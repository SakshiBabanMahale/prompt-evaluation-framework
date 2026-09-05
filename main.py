import json
from evaluator.runner import evaluate_all
from evaluator.report import generate_report

def main():
    with open("data/test_cases.json", "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    results = evaluate_all(test_cases)
    with open("data/results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    report = generate_report(results)
    with open("reports/evaluation_report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print(report)
    print("\nSaved: data/results.json")
    print("Saved: reports/evaluation_report.md")

if __name__ == "__main__":
    main()
