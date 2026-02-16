def is_potential_confusion(pkg, exists, ecosystem, source):
    if exists:
        return False

    if len(pkg) < 4:
        return False

    suspicious_keywords = ["internal", "core", "auth", "shared", "private"]

    if pkg.startswith("@"):
        return True

    if any(word in pkg.lower() for word in suspicious_keywords):
        return True

    return False
