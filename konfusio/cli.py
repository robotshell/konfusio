import argparse

def parse_args():
    parser = argparse.ArgumentParser(prog="konfusio", description="Multi-registry Dependency Confusion hunter")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Single target URL")
    group.add_argument("-l", "--list", help="File with multiple URLs")
    group.add_argument("--js-list", help="File with JS or other source URLs")
    parser.add_argument("--depth", type=int, default=2, help="Crawling depth")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads")
    parser.add_argument("--json", help="Save output to JSON file")
    parser.add_argument("--verbose", action="store_true", help="Verbose mode")
    parser.add_argument("--multi", action="store_true", help="Enable multi-registry scanning")
    parser.add_argument("--aggressive", action="store_true", help="Enable aggressive dependency extraction")

    return parser.parse_args()
