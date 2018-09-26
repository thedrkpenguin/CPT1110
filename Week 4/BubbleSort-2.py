number_of_items = int(input("How many numbers are in the list? "))
                       
number_list = []
    
for x in range(number_of_items):
    number = int(input("Enter a number: "))
    number_list.append(number)

print("Here is the original list ", number_list)

for i in range(len(number_list) - 1, 0, -1): # for i range(9,0,-1)
    for j in range(i): #for j in range(9)
        if number_list[j] < number_list[j + 1]: #if number_list[0] > number_list[0 + 1]
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j] #swapping elements in list
            print (number_list)
