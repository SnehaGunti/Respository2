
#!/usr/bin/env python3
"""
add.py
------
Reads integers from standard input (space-separated), sums them, and writes
the result to 'sum.txt' in the current working directory.

Examples to run locally:
  python3 add.py
  # then type: 10 20 30   (press Enter)

Exit codes:
  0 = success
  2 = invalid input
"""
import sys
from pathlib import Path

OUTPUT_FILE = Path("sum.txt")

def main():
    try:
        raw = input("Enter integers separated by space: ").strip()
        if not raw:
            print("ERROR: No input provided.", file=sys.stderr)
            return 2

        parts = raw.split()
        numbers = [int(p) for p in parts]  # will raise ValueError if not int
    except ValueError:
        print("ERROR: All values must be integers (e.g., 10 20 -3 5).", file=sys.stderr)
        return 2
    except EOFError:
        print("ERROR: No input received on stdin.", file=sys.stderr)
        return 2

    total = sum(numbers)
    OUTPUT_FILE.write_text(str(total), encoding="utf-8")

    print(f"Inputs: {numbers}")
    print(f"Sum = {total} (written to {OUTPUT_FILE.resolve()})")
    return 0

if __name__ == "__main__":
    sys.exit(main())

