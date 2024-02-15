number = int(input("Enter a number: "))

print("Multiplication Table for", number)
for i in range(1, 11):
    product = number * i
    print(number, "x", i, "=", product)