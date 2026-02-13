import re

IMPORT_PATTERNS = [
    r'import\s+(?:.*?\s+from\s+)?[\'"]([^\'"]+)[\'"]',
    r'require\(\s*[\'"]([^\'"]+)[\'"]\s*\)',
    r'import\(\s*[\'"]([^\'"]+)[\'"]\s*\)'
]

def extract_dependencies(js_content):
    packages = set()

    for pattern in IMPORT_PATTERNS:
        matches = re.findall(pattern, js_content)
        for m in matches:
            if not m.startswith((".", "/", "http")):
                packages.add(m)

    return packages
