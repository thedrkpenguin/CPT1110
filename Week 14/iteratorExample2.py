#example of a gernerator

powerTwoList = [x ** 2 for x in range(10)]
for x in powerTwoList:
    print(x)

class custom_range():
    def __init__(self,min_num,max_num):
        #print("In the __init__ function")
        self.__min_num = min_num
        self.__max_num = max_num

    def __iter__(self): #returns the object itself,
                        #invoked 1 time,
                        #starts the iteration
        #print("In the __iter__ function")
        return self
        
    def __next__(self): #returns the next value
                        #continues for desired values
        #print("In the __next__ function")
        if  self.__min_num >= self.__max_num - 1:
            raise StopIteration
        self.__min_num += 1
        return self.__min_num ** 2


for i in custom_range(0,10):
    print(i)
