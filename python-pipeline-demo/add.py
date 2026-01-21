
#!/usr/bin/env python3
# add.py — reads two integers (from piped input or prompts) and writes sum to sum.txt
import sys
from pathlib import Path

sum_path = Path(__file__).with_name("sum.txt")  # sum.txt in the same folder as add.py

data = sys.stdin.read().strip()

if data:
    # Piped input case: e.g., echo "10 20" | python3 add.py
    parts = data.split()
    if len(parts) < 2:
        print("Please provide two integers, e.g., 10 20")
        sys.exit(2)
    a = int(parts[0])
    b = int(parts[1])
else:
    # Interactive fallback (for local testing)
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

total = a + b
sum_path.write_text(str(total), encoding="utf-8")
print("Sum is:", total)

