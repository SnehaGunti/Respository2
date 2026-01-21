
#!/usr/bin/env python3
# check.py — reads sum.txt from the same folder as this script
from pathlib import Path
import sys

sum_path = Path(__file__).with_name("sum.txt")  # sum.txt next to check.py

try:
    total = int(sum_path.read_text(encoding="utf-8").strip())
except FileNotFoundError:
    print(f"sum.txt not found at: {sum_path}")
    sys.exit(2)

if total % 2 == 0:
    print("The number is EVEN → Pipeline SUCCESS")
    sys.exit(0)
else:
    print("The number is ODD → Pipeline FAILURE")
    sys.exit(1)
