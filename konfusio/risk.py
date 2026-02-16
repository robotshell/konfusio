import re

CORPORATE_PATTERNS = [
    r"^@.*\/.*",         # scoped npm
    r".*internal.*",
    r".*corp.*",
    r".*private.*",
    r".*auth.*",
    r".*core.*",
    r".*shared.*"
]

def is_potential_confusion(pkg, exists, ecosystem, source):
    if exists:
        return False

    if len(pkg) < 4:
        return False

    for pattern in CORPORATE_PATTERNS:
        if re.match(pattern, pkg.lower()):
            return True

    return False
