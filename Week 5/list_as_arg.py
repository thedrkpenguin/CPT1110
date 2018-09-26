def SUM_MY_LIST(NUMBER_LIST):
    TOTAL = 0
    for x in NUMBER_LIST:
        TOTAL += x
    return TOTAL

print("The sum of the list is: ", SUM_MY_LIST([1,2,3,4,5])) #15

NUMBER_LIST = [1,2,4,5,6]

print("The sum of the list is: ", SUM_MY_LIST(NUMBER_LIST)) #18

print("The sum of the list is: ", SUM_MY_LIST(5)) #TypeError
