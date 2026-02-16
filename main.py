from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from urllib.parse import urlparse

from konfusio.cli import parse_args
from konfusio.crawler import crawl
from konfusio.fetcher import fetch
from konfusio.detector import detect_ecosystem
from konfusio.registry_router import check_registry
from konfusio.risk import is_potential_confusion
from konfusio.output import print_results, export_json


def analyze_target(url, threads):
    findings = []

    discovered_files = crawl(url)

    if not discovered_files:
        return findings

    for file_url in tqdm(discovered_files, desc=f"Analyzing files ({urlparse(url).netloc})", leave=False):
        content = fetch(file_url)
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


def load_targets(args):
    if args.url:
        return [args.url]

    targets = []
    with open(args.list) as f:
        for line in f:
            line = line.strip()
            if line:
                targets.append(line)

    return targets


def main():
    args = parse_args()

    targets = load_targets(args)

    all_findings = []

    for target in tqdm(targets, desc="Scanning targets"):
        results = analyze_target(target, args.threads)
        all_findings.extend(results)

    print_results(all_findings)

    if args.json:
        export_json(all_findings, args.json)


if __name__ == "__main__":
    main()
