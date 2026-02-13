def calculate_score_multi(package, registry_results, company_hint=None, private_registry=False):
    score = 0

    for registry, exists in registry_results.items():
        if not exists:
            score += 5

    if private_registry:
        score += 5

    if company_hint and company_hint in package.lower():
        score += 3

    if score >= 8:
        severity = "HIGH"
    elif score >= 4:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return score, severity
