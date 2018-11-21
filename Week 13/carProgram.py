class Car():
    def __init__(self,make,year,appraised_value):
        self.make = make #public
        self.year = year #public
        self.appraised_value = appraised_value #public
        #self.__appraised_value = appraised_value #private

    def set_make(self,make):
        self.make = make

    def set_year(self,year):
        self.year = year
        
    def set_value(self,appraised_value):
        self.appraised_value = appraised_value
        #self.__appraised_value = appraised_value

    def get_make(self):
        return self.make

    def get_year(self):
        return self.year
    
    #def __get_year(self):
        #return self.year

    def get_value(self):
        return self.appraised_value
        #return self.__appraised_value

my_car = Car("Dodge", "2014","$5")
print(my_car.get_make())
print(my_car.get_year()) #can execute because it is public
#print(my_car.__get_year()) #cannot execute because it is public
print(my_car.get_value())
print("Changed values (below) between Public vs Private variables and methods")
print("-" * 20)
my_car.appraised_value = "$1M"  #changing the variable value due to being public
#my_car.__appraised_value = "$1M" #cannot be changed due to being private
print(my_car.get_value())


"""print("-" * 20)

my_car.set_make("BMW")
my_car.set_year("2017")
print(my_car.get_make())
print(my_car.get_year())

"""
