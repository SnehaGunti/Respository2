
# add.py

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b

with open("sum.txt", "w") as f:
    f.write(str(total))

print("Sum is:", total)

