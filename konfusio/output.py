from colorama import Fore, Style, init
init(autoreset=True)

def print_results(results, target=None):
    if target:
        print(f"\nTarget: {target}")
    print(f"Dependencies found: {len(results)}\n")

    for r in results:
        severity = r.get("severity", "UNKNOWN")
        name = r.get("name")
        registries = r.get("registries", {})
        score = r.get("score", 0)

        # Color según severidad
        if severity == "HIGH":
            color = Fore.RED
        elif severity == "MEDIUM":
            color = Fore.YELLOW
        else:
            color = Fore.GREEN

        # Formatear registries
        reg_str = ", ".join(f"{k}:{'Yes' if v else 'No'}" for k, v in registries.items())

        print(color + f"[{severity}] {name} (Registries: {reg_str}, Score: {score})")
