from colorama import Fore, Style, init

init(autoreset=True)

def print_results(results, target=None):
    if target:
        print(f"\nTarget: {target}")

    if not results:
        print("No dependencies found.")
        return

    high = medium = low = 0

    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        if r["severity"] == "HIGH":
            color = Fore.RED
            high += 1
        elif r["severity"] == "MEDIUM":
            color = Fore.YELLOW
            medium += 1
        else:
            color = Fore.GREEN
            low += 1

        print(color + f"[{r['severity']}] {r['name']} (Exists: {r['exists']}, Score: {r['score']})")

    print("\nSummary:")
    print(f"HIGH: {high} | MEDIUM: {medium} | LOW: {low}")
