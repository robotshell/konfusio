import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Konfusio - Multi Ecosystem Dependency Confusion Scanner")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Single URL to analyze")
    group.add_argument("-f", "--file", help="File containing URLs")

    parser.add_argument("--threads", type=int, default=10)

    return parser.parse_args()
