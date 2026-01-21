
#!/usr/bin/env python3
"""
check.py
--------
Reads the integer sum from 'sum.txt' and exits with:
  0 if even (pipeline SUCCESS)
  1 if odd  (pipeline FAILURE)
  2 if read/parse error (treat as infra/config error)

Usage:
  python3 check.py
"""
import sys
from pathlib import Path

INPUT_FILE = Path("sum.txt")

def main():
    if not INPUT_FILE.exists():
        print(f"ERROR: {INPUT_FILE} not found. Run add.py first.", file=sys.stderr)
        return 2

    try:
        content = INPUT_FILE.read_text(encoding="utf-8").strip()
        total = int(content)
    except Exception as e:
        print(f"ERROR: Failed to read/parse {INPUT_FILE}: {e}", file=sys.stderr)
        return 2

    if total % 2 == 0:
        print(f"SUM = {total} ➜ Even ➜ Pipeline PASS")
        return 0
    else:
        print(f"SUM = {total} ➜ Odd ➜ Pipeline FAIL (exit 1)")
        return 1

if __name__ == "__main__":
    sys.exit(main())

