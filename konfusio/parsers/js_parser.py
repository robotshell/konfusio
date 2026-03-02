import re

IMPORT_REGEX = [
    r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]',
    r'require\([\'"]([^\'"]+)[\'"]\)',
    r'import\([\'"]([^\'"]+)[\'"]\)'
]

def parse_js(content):
    packages = set()

    for pattern in IMPORT_REGEX:
        matches = re.findall(pattern, content)
        for m in matches:
            m = m.strip()

            # Exclude local/relative paths only
            if m.startswith((".", "/")):
                continue

            packages.add(m)

    return packages
