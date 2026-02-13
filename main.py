import requests
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor

from konfusio.cli import parse_args
from konfusio.crawler import crawl_for_js
from konfusio.parser import (
    extract_dependencies,
    extract_registries,
    extract_sourcemap_url,
    extract_from_sourcemap,
)
from konfusio.registry_manager import check_all_registries
from konfusio.scorer import calculate_score_multi
from konfusio.output import print_results


def get_company_hint(url):
    domain = urlparse(url).netloc
    return domain.split(".")[0].lower()


def fetch(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except:
        return ""


def analyze_js(js_url):
    content = fetch(js_url)
    if not content:
        return set(), set(), False

    packages = extract_dependencies(content)
    private_registry_detected = bool(extract_registries(content))

    # Sourcemap handling
    sm_url = extract_sourcemap_url(content)
    if sm_url:
        full_sm_url = urljoin(js_url, sm_url)
        sm_content = fetch(full_sm_url)
        packages.update(extract_from_sourcemap(sm_content))

    return packages, private_registry_detected


def main():
    args = parse_args()

    if args.url:
        target = args.url
        company_hint = get_company_hint(target)
        js_urls = crawl_for_js(target, depth=args.depth)

    elif args.list:
        js_urls = set()
        target = None
        company_hint = None
        with open(args.list) as f:
            for line in f:
                url = line.strip()
                if url.endswith(".js"):
                    js_urls.add(url)
                else:
                    js_urls.update(crawl_for_js(url, depth=args.depth))

    elif args.js_list:
        target = None
        company_hint = None
        with open(args.js_list) as f:
            js_urls = {line.strip() for line in f}

    all_packages = set()
    private_registry_detected = False

    # Threaded analysis
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(analyze_js, js) for js in js_urls]
        for future in futures:
            packages, private = future.result()
            all_packages.update(packages)
            if private:
                private_registry_detected = True

    results = []

    # Threaded multi-registry check
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(check_all_registries, pkg): pkg for pkg in all_packages}
        for future in futures:
            pkg = futures[future]
            registry_results = future.result()
            score, severity = calculate_score_multi(
                pkg,
                registry_results,
                company_hint=company_hint,
                private_registry=private_registry_detected
            )
            results.append({
                "name": pkg,
                "registries": registry_results,
                "score": score,
                "severity": severity
            })

    print_results(results, target)


if __name__ == "__main__":
    main()
