import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog="konfusio",
        description="Multi-ecosystem Dependency Confusion Scanner"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Single target URL")
    group.add_argument("-l", "--list", help="File containing list of target URLs")

    parser.add_argument("--threads", type=int, default=5)
    parser.add_argument("--json", help="Export results to JSON file")

    return parser.parse_args()
