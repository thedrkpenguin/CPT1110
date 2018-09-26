#Name
#Date
#Program Name
#Pseudocode

#Need to prompt user for month budget
#Prompt for thier expenses
#Add up their expenses
#Under/Over budget and by how much

def UNDER_BUDGET(MONTHLY_BUDGET,TOTAL_EXPENSES):
    return MONTHLY_BUDGET - TOTAL_EXPENSES
    #for example... return a,b,c
    
def OVER_BUDGET(MONTHLY_BUDGET,TOTAL_EXPENSES):
    DIFFERENCE = TOTAL_EXPENSES - MONTHLY_BUDGET
    return DIFFERENCE
    
def ON_BUDGET(MONTHLY_BUDGET,TOTAL_EXPENSES):
    return "Good Budgeting"
    
def main():
    #CONTINUE = 'y'
    EXPENSES = 1.0
    MONTHLY_BUDGET = float(input("Please enter monthly budget: "))
    TOTAL_EXPENSES = 0.0
    #while CONTINUE == 'y':

    while EXPENSES != 0.0:
        EXPENSES = float(input("Enter a monthly expense: "))
        #CONTINUE = str(input("Do you have additional expenses y/n? "))
        TOTAL_EXPENSES += EXPENSES
        #TOTAL_EXPENSES = TOTAL_EXPENSES + EXPENSES

    print("Monthly Budget: $",format(MONTHLY_BUDGET,',.2f'),sep="")
    print("Spent: $",format(TOTAL_EXPENSES,',.2f'),sep="")

    if MONTHLY_BUDGET > TOTAL_EXPENSES:
        DIFFERENCE = UNDER_BUDGET(MONTHLY_BUDGET,TOTAL_EXPENSES)
        print("You are $",format(DIFFERENCE,'.2f')," under budget",sep="")
        
    elif MONTHLY_BUDGET < TOTAL_EXPENSES:
        print("You are $",format(OVER_BUDGET(MONTHLY_BUDGET,TOTAL_EXPENSES)\
                                 ,'.2f')," over budget",sep="")
    else:
        DIFFERENCE = ON_BUDGET(MONTHLY_BUDGET,TOTAL_EXPENSES)
        print(DIFFERENCE)

main()

