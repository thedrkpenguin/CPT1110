a = 5
b = 6
c = 7


print(a == 5 or b == 6 and c == 7) #True: b==6 and c==7 is true, a==5 or true is true
print(a == 6 or b == 6 and c == 7) #True: b==6 and c==7 is true, a==6 or true is true
print(a == 5 or b == 6 and c == 8) #True: b==6 and c==8 is false, a==5 or false is true
print(a == 6 or b == 6 and c == 8) #False: b==6 and c==8 is false, a==6 or false is false
print((a == 5 or b == 6) and c == 8)#False: parenthses make the or evaluate first, then the and

#Great link for operator precedence
#http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html
