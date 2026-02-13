import requests
from urllib.parse import urlparse

from konfusio.cli import parse_args
from konfusio.crawler import crawl_for_js
from konfusio.parser import extract_dependencies
from konfusio.registry import check_package
from konfusio.scorer import calculate_score
from konfusio.output import print_results, save_json

def get_company_hint(url):
    domain = urlparse(url).netloc
    return domain.split(".")[0].lower()

def fetch_js(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except:
        return ""

def process_js_list(js_urls, company_hint):
    packages = set()

    for js in js_urls:
        content = fetch_js(js)
        deps = extract_dependencies(content)
        packages.update(deps)

    results = []

    for package in packages:
        exists = check_package(package)
        score, severity = calculate_score(package, exists, company_hint)

        results.append({
            "name": package,
            "exists": exists,
            "score": score,
            "severity": severity
        })

    return results

def main():
    args = parse_args()

    if args.url:
        company_hint = get_company_hint(args.url)
        js_urls = crawl_for_js(args.url, depth=args.depth)

    elif args.list:
        js_urls = set()
        company_hint = None
        with open(args.list) as f:
            for line in f:
                url = line.strip()
                if url.endswith(".js"):
                    js_urls.add(url)
                else:
                    js_urls.update(crawl_for_js(url, depth=args.depth))

    elif args.js_list:
        company_hint = None
        with open(args.js_list) as f:
            js_urls = {line.strip() for line in f}

    results = process_js_list(js_urls, company_hint)

    print_results(results)

    if args.json:
        save_json(results, args.json)

if __name__ == "__main__":
    main()
