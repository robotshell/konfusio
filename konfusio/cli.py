import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog="konfusio",
        description="Multi-ecosystem Dependency Confusion Scanner"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Single target URL")
    group.add_argument("-l", "--list", help="File containing list of URLs")

    parser.add_argument("--threads", type=int, default=5)
    parser.add_argument("--json", help="Export results to JSON file")
    parser.add_argument("--js-mode", action="store_true", help="Force JS mode (treat input as direct JS URLs)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    return parser.parse_args()
