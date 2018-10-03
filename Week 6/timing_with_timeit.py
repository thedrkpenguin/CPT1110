import timeit

def list_process():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    for i in my_list:
        print(i)
  

def tuple_process():
    my_tuple = (1,2,3,4,5,6,7,8,9,10)
    for i in my_tuple:
        print(i)


print(timeit.timeit(list_process,number=1))

print(timeit.timeit(tuple_process,number=1))
