from colorama import Fore, Style, init
init(autoreset=True)

def print_results(results, target=None):
    if target:
        print(f"\nTarget: {target}")
    print(f"Dependencies found: {len(results)}\n")

    for r in results:
        severity = r.get("severity", "UNKNOWN")
        name = r.get("name")
        source = r.get("source", "Unknown")
        registries = r.get("registries", {})
        score = r.get("score", 0)
        potential = r.get("potential_confusion", False)

        # Color según severidad
        if severity == "HIGH":
            color = Fore.RED
        elif severity == "MEDIUM":
            color = Fore.YELLOW
        else:
            color = Fore.GREEN

        reg_str = ", ".join(f"{k}:{'Yes' if v else 'No'}" for k, v in registries.items())
        confusion_marker = Fore.MAGENTA + "[POTENTIAL DEPENDENCY CONFUSION]" if potential else ""

        print(color + f"[{severity}] {name} (Source: {source}, Registries: {reg_str}, Score: {score}) {confusion_marker}")
