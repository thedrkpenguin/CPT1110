a = 90
b = 80
c = 70
grade = 68

if a == 5:
    if b == 11:
        print("A is equal to 5 and B is equal to 10")
    else:
        if c == 16:
            print("B is not equal to 10 and C is equal to 15")
        else:
            print("B is not equal to 10 and C is not equal to 15")
else:
    print("A is not equal to 5")


if grade <= 59:
    print("E")
elif grade <= 69:
    print("D")
elif grade <= 79:
    print("C")
elif grade <= 89:
    print("B")
elif grade <= 100:
    print("A")
else:
    print("No grade")
