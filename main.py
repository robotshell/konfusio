from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from konfusio.cli import parse_args
from konfusio.fetcher import fetch
from konfusio.detector import detect_ecosystem
from konfusio.registry_router import check_registry
from konfusio.risk import is_potential_confusion
from konfusio.output import print_results


def main():
    args = parse_args()

    targets = []
    if args.url:
        targets.append(args.url)
    elif args.file:
        with open(args.file) as f:
            targets = [x.strip() for x in f if x.strip()]

    findings = []

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(fetch, url): url for url in targets}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Fetching targets"):
            url = futures[future]
            content = future.result()

            ecosystem, parser = detect_ecosystem(url, content)
            if not ecosystem:
                continue

            packages = parser(content)

            for pkg in packages:
                exists = check_registry(pkg, ecosystem)

                if is_potential_confusion(pkg, exists, ecosystem, url):
                    findings.append({
                        "package": pkg,
                        "ecosystem": ecosystem,
                        "source": url
                    })

    print_results(findings)


if __name__ == "__main__":
    main()
