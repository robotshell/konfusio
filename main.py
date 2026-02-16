from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from konfusio.cli import parse_args
from konfusio.crawler import crawl
from konfusio.fetcher import fetch
from konfusio.detector import detect_ecosystem
from konfusio.registry_router import check_registry
from konfusio.risk import is_potential_confusion
from konfusio.output import print_results, export_json


def analyze_target(url, threads):
    discovered_files = crawl(url)

    findings = []

    for file_url in tqdm(discovered_files, desc="Analyzing files"):
        content = fetch(file_url)
        ecosystem, parser = detect_ecosystem(file_url, content)

        if not ecosystem:
            continue

        packages = parser(content)

        for pkg in packages:
            exists = check_registry(pkg, ecosystem)

            if is_potential_confusion(pkg, exists, ecosystem, file_url):
                findings.append({
                    "package": pkg,
                    "ecosystem": ecosystem,
                    "source_file": file_url
                })

    return findings


def main():
    args = parse_args()

    results = analyze_target(args.url, args.threads)

    print_results(results)

    if args.json:
        export_json(results, args.json)


if __name__ == "__main__":
    main()
