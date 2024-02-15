employee_dict = {}

while True:
    name = input("Enter the name of the employee: ")
    if name.lower() == "no":
        break

    salary = float(input("Enter the salary of the employee: "))
    employee_dict[name] = salary

print("\nEmployee Dictionary:")
for name, salary in employee_dict.items():
    print(f"{name}: {salary}")