def main():
    FIRST_AGE = int(input("Enter your age: "))
    SECOND_AGE = int(input("Enter your friends age: "))
    TOTAL = SUM_AGES(FIRST_AGE, SECOND_AGE)
    print("The total is: ", TOTAL)

def SUM_AGES(FIRST_AGE, SECOND_AGE):
    #TOTAL = FIRST_AGE + SECOND_AGE
    #return TOTAL
    return FIRST_AGE + SECOND_AGE
main()
    
