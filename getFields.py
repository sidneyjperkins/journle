import re
from collections import Counter

def count_fields(filename="index.html"):
    with open(filename, "r", encoding="utf-8") as f:
        content = "\n".join(
            line for line in f
            if not re.match(r'^\s*//', line)
        )

    # Match patterns like: field: "cardiology" or field:'oncology'
    pattern = re.compile(r'field\s*:\s*["\']([^"\']+)["\']')
    fields = pattern.findall(content)

    if not fields:
        print("No fields found.")
        return

    counts = Counter(fields)
    total = sum(counts.values())

    print(f"Total fields found: {total}\n")
    print("Field distribution:")
    print("-" * 30)

    for field, count in counts.most_common():
        proportion = count / total * 100
        print(f"{field:20} {count:3d} ({proportion:5.1f}%)")

if __name__ == "__main__":
    count_fields()
