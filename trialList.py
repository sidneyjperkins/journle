import re
import csv

def extract_trials_to_csv(
    input_file="index.html",
    output_file="trials.csv"
):
    with open(input_file, "r", encoding="utf-8") as f:
        content = "\n".join(
            line for line in f
            if not re.match(r'^\s*//', line)
        )

    # Match JS objects containing name and field (order-independent)
    pattern = re.compile(
        r'name\s*:\s*["\']([^"\']+)["\'].*?'
        r'field\s*:\s*["\']([^"\']+)["\']'
        r'|'
        r'field\s*:\s*["\']([^"\']+)["\'].*?'
        r'name\s*:\s*["\']([^"\']+)["\']',
        re.DOTALL
    )

    rows = []

    for match in pattern.findall(content):
        # Match groups depend on which side of the OR matched
        name = match[0] or match[3]
        field = match[1] or match[2]
        rows.append((name, field))

    if not rows:
        print("No trials found.")
        return

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["trial_name", "field"])
        writer.writerows(rows)

    print(f"Saved {len(rows)} trials to {output_file}")

if __name__ == "__main__":
    extract_trials_to_csv()