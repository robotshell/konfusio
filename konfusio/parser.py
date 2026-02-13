import re
import json

IMPORT_PATTERNS = [
    r'import\s+(?:.*?\s+from\s+)?[\'"]([^\'"]+)[\'"]',
    r'require\(\s*[\'"]([^\'"]+)[\'"]\s*\)',
    r'import\(\s*[\'"]([^\'"]+)[\'"]\s*\)'
]

REGISTRY_PATTERNS = [
    r'registry\s*:\s*[\'"]([^\'"]+)',
    r'npm\.[a-zA-Z0-9.-]+',
    r'artifactory\.[a-zA-Z0-9.-]+',
    r'verdaccio\.[a-zA-Z0-9.-]+'
]


def normalize_package(pkg):
    if "/" in pkg and not pkg.startswith("@"):
        return pkg.split("/")[0]
    return pkg


def is_valid_package(pkg):
    if pkg.startswith((".", "/", "http")):
        return False
    if len(pkg) < 2:
        return False
    return True


def extract_dependencies(js_content):
    packages = set()

    for pattern in IMPORT_PATTERNS:
        matches = re.findall(pattern, js_content)
        for m in matches:
            if is_valid_package(m):
                packages.add(normalize_package(m))

    return packages


def extract_registries(js_content):
    found = set()
    for pattern in REGISTRY_PATTERNS:
        matches = re.findall(pattern, js_content)
        for m in matches:
            found.add(m)
    return found


def extract_sourcemap_url(js_content):
    match = re.search(r'//# sourceMappingURL=(.*)', js_content)
    if match:
        return match.group(1).strip()
    return None


def extract_from_sourcemap(map_content):
    try:
        data = json.loads(map_content)
        sources = data.get("sources", [])
        return {s for s in sources if "/" in s}
    except:
        return set()
