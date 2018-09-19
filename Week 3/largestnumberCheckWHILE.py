num = 0
max_num = 0

CONTINUE = 'y'

while CONTINUE == 'y':
    num = int(input("Enter a value for number: "))
    if num > max_num:
        max_num = num
    CONTINUE = input("Would you like to continue y/n? ")

print("The largest number entered is ", max_num)




