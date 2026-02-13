import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog="konfusio",
        description="Minimal Dependency Confusion Hunter"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Single target URL")
    group.add_argument("-l", "--list", help="File containing URLs")
    group.add_argument("--js-list", help="File containing JS URLs")

    parser.add_argument("--depth", type=int, default=2, help="Crawling depth")
    parser.add_argument("--threads", type=int, default=10, help="Thread count")
    parser.add_argument("--json", help="JSON output file")
    parser.add_argument("--verbose", action="store_true")

    return parser.parse_args()
