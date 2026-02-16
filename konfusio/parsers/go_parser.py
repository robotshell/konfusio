def parse_go_mod(content):
    packages = set()

    for line in content.splitlines():
        if line.startswith("require"):
            parts = line.split()
            if len(parts) >= 2:
                packages.add(parts[1])

    return packages
