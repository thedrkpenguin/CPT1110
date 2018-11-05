def show_double(num1,num2,num3):
    print("Num1 --> ", num1)
    print("Num2 --> ", num2)
    print("Num3 --> ", num3)
    
    result = (num1 + num2) / num3
    print("The result of the double is: ", result)


def main():
    num1 = int(input("Enter an integer: ")) #locally significant only
    num2 = int(input("Enter an integer: "))
    num3 = int(input("Enter an integer: "))
    show_double(num1,num2=num2,num3=num3)


main()
