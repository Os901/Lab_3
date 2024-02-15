number_list = []


for i in range(10):
    number = float(input("Enter a number: "))
    number_list.append(number)


largest_number = number_list[0]


for number in number_list:
    if number > largest_number:
        largest_number = number

print("The largest number is:", largest_number)