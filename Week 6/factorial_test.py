"""
def factorial(number):
    if number <= 0:
        return
    if number < 2:
        return 1
    product = 1

    for i in range(2, number + 1):
        product *= i
    return product

for num in range(1,6):
    print("The factorial is: ",num,factorial(num))

"""

def factorial(number):
    if number <=0:
        return
    if number < 2:
        return 1
    
    return number * factorial(number - 1)

number = 5
print("The factorial for ",number, "is" ,factorial(number))

    
    

   
