from colorama import Fore, init
init(autoreset=True)

def print_results(findings):
    if not findings:
        print("\nNo potential Dependency Confusion detected.")
        return

    print("\n🔥 Potential Dependency Confusion Findings:\n")

    for f in findings:
        print(Fore.RED + "----------------------------------------")
        print(Fore.YELLOW + f"Package   : {f['package']}")
        print(Fore.CYAN + f"Ecosystem : {f['ecosystem']}")
        print(Fore.GREEN + f"Source    : {f['source']}")
