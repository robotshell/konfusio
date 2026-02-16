def parse_requirements(content):
    packages = set()

    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            pkg = line.split("==")[0].strip()
            packages.add(pkg)

    return packages
