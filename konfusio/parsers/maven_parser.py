import re

def parse_maven(content):
    matches = re.findall(
        r"<groupId>(.*?)</groupId>.*?<artifactId>(.*?)</artifactId>",
        content,
        re.DOTALL
    )

    packages = set()
    for group, artifact in matches:
        packages.add(f"{group}:{artifact}")

    return packages
