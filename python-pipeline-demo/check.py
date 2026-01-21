
#!/usr/bin/env python3

with open("sum.txt", "r") as f:
    total = int(f.read())

if total % 2 == 0:
    print("The number is EVEN → Pipeline SUCCESS")
    exit(0)
else:
    print("The number is ODD → Pipeline FAILURE")
    exit(1)

