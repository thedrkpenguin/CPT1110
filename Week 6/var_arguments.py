def calculate(*args):
    total = 0
    for number in args:
        total += number
    return total

print("The sum of the numbers is: ",calculate(3,5))
print("The sum of the numbers is: ",calculate(1,2,3,4,5))
print("The sum of the numbers is: ",calculate(6))
