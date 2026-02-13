def calculate_score(package, exists_publicly, company_hint=None):
    score = 0

    if package.startswith("@"):
        score += 2

    if company_hint and company_hint in package.lower():
        score += 3

    if not exists_publicly:
        score += 5

    if score >= 8:
        severity = "HIGH"
    elif score >= 4:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return score, severity
