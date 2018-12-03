my_list = [x for x in range(10)]

print("This is a list generated with list comprehension: ", end = " ")
print(my_list)


def usingYield():
    my_list = range(10)
    for i in my_list:
        yield i

def usingReturn():
    my_list = range(10)
    for i in my_list:
        return i

my_yield_list = usingYield()
my_return_list = usingReturn()

print("This is a list generated with the yield statement: ", end = " ")
for num in my_yield_list:
    print(num,end = ",")

print()
print("This is a list generated with the return statement: ", end = " ")

"""
for num in my_return_list: #This will return a not iterable error as only one
                            #value is returned, not a sequence
    print(num, end = " ")
    
"""
print(my_return_list) #This will return the first value only in the loop
                      #This is because return will break the loop after
                      #its first run
