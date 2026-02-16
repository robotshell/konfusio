from tqdm import tqdm
from urllib.parse import urlparse

from konfusio.cli import parse_args
from konfusio.crawler import crawl
from konfusio.fetcher import fetch
from konfusio.parsers.js_parser import parse_js
from konfusio.registry_router import check_registry
from konfusio.risk import is_potential_confusion
from konfusio.output import print_results, export_json


def analyze_js_list(js_urls):
    findings = []

    for file_url in tqdm(js_urls, desc="Analyzing JS files"):
        content = fetch(file_url)

        if not content:
            continue

        packages = parse_js(content)

        for pkg in packages:
            exists = check_registry(pkg, "npm")

            if is_potential_confusion(pkg, exists, "npm", file_url):
                findings.append({
                    "target": file_url,
                    "package": pkg,
                    "ecosystem": "npm",
                    "source_file": file_url
                })

    return findings


def analyze_target(url):
    findings = []

    discovered_files = crawl(url)

    for file_url in tqdm(discovered_files,
                         desc=f"Analyzing files ({urlparse(url).netloc})",
                         leave=False):

        content = fetch(file_url)
        if not content:
            continue

        from konfusio.detector import detect_ecosystem
        ecosystem, parser = detect_ecosystem(file_url, content)

        if not ecosystem or not parser:
            continue

        packages = parser(content)

        for pkg in packages:
            exists = check_registry(pkg, ecosystem)

            if is_potential_confusion(pkg, exists, ecosystem, file_url):
                findings.append({
                    "target": url,
                    "package": pkg,
                    "ecosystem": ecosystem,
                    "source_file": file_url
                })

    return findings


def load_list(path):
    targets = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                targets.append(line)
    return targets


def main():
    args = parse_args()

    all_findings = []

    if args.js_mode:
        if args.list:
            js_urls = load_list(args.list)
        else:
            js_urls = [args.url]

        results = analyze_js_list(js_urls)
        all_findings.extend(results)

    else:
        if args.url:
            targets = [args.url]
        else:
            targets = load_list(args.list)

        for target in tqdm(targets, desc="Scanning targets"):
            results = analyze_target(target)
            all_findings.extend(results)

    print_results(all_findings)

    if args.json:
        export_json(all_findings, args.json)


if __name__ == "__main__":
    main()
