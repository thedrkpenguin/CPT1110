#lambda function?  function without a name (anonymous functions)
#lambda parameters : expression

double_num = lambda : 2  #parameterless function
#def double_num():

squares = lambda x : x * x #needs one parameter
#def squares(x):
#   return x * x

exponents = lambda x,y : x ** y #needs two parameters
#def exponents(x,y):
#   return x ** y

print(squares(5))
print(exponents(3,5))

list1 = [x for x in range(10)]
#map(function,list)
list2 = list(map(lambda x : x ** 2, list1))  #list2 = [x ** 2 for x in range(10)]
print(list1)
print(list2)

list3 = [x for x in range(10)]
#filter(function,list)
even_number_list = list(filter(lambda x : x >= 0 and x % 2 == 0, list3))
#even_number_list = [x for x in range(10) if x % 2 == 0]
print(even_number_list)



