num1 = 0
num2 = 0
num3 = 0
num4 = 0

num1 = int(input("Enter a value for number 1: "))
num2 = int(input("Enter a value for number 2: "))
num3 = int(input("Enter a value for number 3: "))
num4 = int(input("Enter a value for number 4: "))

max_num = num1

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

if num4 > max_num:
    max_num = num4

print("The largest number entered is ", max_num)




