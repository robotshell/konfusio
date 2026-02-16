from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from konfusio.cli import parse_args
from konfusio.fetcher import fetch
from konfusio.parsers.js_parser import parse_js
from konfusio.registry_router import check_registry
from konfusio.risk import is_potential_confusion
from konfusio.output import print_results, export_json

def analyze_single_js(file_url, verbose=False):
    findings = []
    if verbose:
        print(f"[VERBOSE] Analyzing JS file: {file_url}")
    content = fetch(file_url)
    if not content:
        if verbose:
            print(f"[VERBOSE] Failed to fetch {file_url}")
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

def analyze_js_list_parallel(js_urls, threads=10, verbose=False):
    all_findings = []
    seen_urls = set()
    js_urls = [u for u in js_urls if u not in seen_urls and not seen_urls.add(u)]

    if verbose:
        print(f"[VERBOSE] Starting JS mode with {len(js_urls)} files, using {threads} threads")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(analyze_single_js, url, verbose): url for url in js_urls}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Analyzing JS files"):
            all_findings.extend(future.result())

    if verbose:
        print("[VERBOSE] Finished analyzing JS files")
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

        if args.verbose:
            print(f"[VERBOSE] Running in JS mode")
        all_findings = analyze_js_list_parallel(js_urls, threads=args.threads, verbose=args.verbose)

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
            if args.verbose:
                print(f"[VERBOSE] Crawling target: {target}")
            discovered_files = crawl(target)
            if args.verbose:
                print(f"[VERBOSE] Found {len(discovered_files)} files at {target}")

            for file_url in tqdm(discovered_files,
                                 desc=f"Analyzing files ({urlparse(target).netloc})",
                                 leave=False):
                if args.verbose:
                    print(f"[VERBOSE] Fetching file: {file_url}")
                content = fetch(file_url)
                if not content:
                    if args.verbose:
                        print(f"[VERBOSE] Failed to fetch {file_url}")
                    continue

                ecosystem, parser = detect_ecosystem(file_url, content)
                if not ecosystem or not parser:
                    if args.verbose:
                        print(f"[VERBOSE] Unknown ecosystem for {file_url}")
                    continue

                packages = parser(content)
                if args.verbose:
                    print(f"[VERBOSE] Found {len(packages)} packages in {file_url}")

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
