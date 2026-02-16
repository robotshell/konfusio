import re

IMPORT_REGEX = [
    r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]',
    r'require\([\'"]([^\'"]+)[\'"]\)'
]

def parse_js(content):
    packages = set()

    for pattern in IMPORT_REGEX:
        matches = re.findall(pattern, content)
        for m in matches:
            if not m.startswith(".") and "/" not in m:
                packages.add(m.strip())

    return packages
