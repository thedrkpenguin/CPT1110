TWO_D_LIST = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14]]

print(TWO_D_LIST[0]) #print first inner list
print(TWO_D_LIST[1]) #print second inner list
print(TWO_D_LIST[2]) #print third inner list
print(TWO_D_LIST[3]) #print forth inner list

#printing [row][column] --> both start at 0 so row 1, column 3 is the number 8
print(TWO_D_LIST[1][3])

#To print the number 6 use the following statement
print(TWO_D_LIST[1][1])

TWO_D_LIST[1][2] = 100
TWO_D_LIST[0] = [100,200,300,400]

print(TWO_D_LIST)
