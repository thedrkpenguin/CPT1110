A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

GRADE = float(input("Enter your test score: "))

if GRADE >= A_SCORE:
    print("Your grade is an A")
elif GRADE >= B_SCORE:
    print("Your grade is a B")
elif GRADE >= C_SCORE:
    print("Your grade is a C")
elif GRADE >= D_SCORE:
    print("Your grade is a D")
else:
    print("Your grade is an E")
