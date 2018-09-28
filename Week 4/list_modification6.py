NUMBER_LIST = [5,8,2,4,9,1,3,7,6,0]

print("The lowest value in the list is: ", min(NUMBER_LIST))

print("The maximum value in the list is: ", max(NUMBER_LIST))

print("The sum of the values in the list is: ", sum(NUMBER_LIST))

print("The length of the list is: ", len(NUMBER_LIST))

print("The average of the values in the list is: ", (sum(NUMBER_LIST) / len(NUMBER_LIST)))

NUMBER_LIST.sort()
print("Ascending order of the values in the list is: ", NUMBER_LIST)

NUMBER_LIST.reverse()
print("Descending order of the vallues in the list is: ", NUMBER_LIST)

