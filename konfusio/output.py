import json

def print_results(results):
    for r in results:
        print(f"[{r['severity']}] {r['name']} | Exists: {r['exists']} | Score: {r['score']}")

def save_json(results, filename):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
