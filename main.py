from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from konfusio.cli import parse_args
from konfusio.fetcher import fetch
from konfusio.parsers.js_parser import parse_js
from konfusio.registry_router import check_registry
from konfusio.risk import is_potential_confusion
from konfusio.output import print_results, export_json


def analyze_single_js(file_url):
    findings = []
    content = fetch(file_url)
    if not content:
        return findings

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


def analyze_js_list_parallel(js_urls, threads=10):
    all_findings = []
    seen_urls = set()
    js_urls = [u for u in js_urls if u not in seen_urls and not seen_urls.add(u)]

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(analyze_single_js, url): url for url in js_urls}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Analyzing JS files"):
            all_findings.extend(future.result())

    return all_findings


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

        all_findings = analyze_js_list_parallel(js_urls, threads=args.threads)

    else:
        from tqdm import tqdm
        from urllib.parse import urlparse
        from konfusio.crawler import crawl
        from konfusio.detector import detect_ecosystem

        if args.url:
            targets = [args.url]
        else:
            targets = load_list(args.list)

        for target in tqdm(targets, desc="Scanning targets"):
            discovered_files = crawl(target)
            for file_url in tqdm(discovered_files,
                                 desc=f"Analyzing files ({urlparse(target).netloc})",
                                 leave=False):
                content = fetch(file_url)
                if not content:
                    continue
                ecosystem, parser = detect_ecosystem(file_url, content)
                if not ecosystem or not parser:
                    continue
                packages = parser(content)
                for pkg in packages:
                    exists = check_registry(pkg, ecosystem)
                    if is_potential_confusion(pkg, exists, ecosystem, file_url):
                        all_findings.append({
                            "target": target,
                            "package": pkg,
                            "ecosystem": ecosystem,
                            "source_file": file_url
                        })

    print_results(all_findings)

    if args.json:
        export_json(all_findings, args.json)


if __name__ == "__main__":
    main()
