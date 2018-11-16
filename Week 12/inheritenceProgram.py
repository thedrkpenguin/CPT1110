class Mammal():
    def __init__(self,species):
        self.species = species

    def display_species(self):
        print("I am a ", self.species)

    def make_sound(self):
        print("Grrrrr")

class Dog(Mammal):
    def __init__(self,age):
        self.age = age
        #Mammal.__init__(self,'Dog')
        super().__init__('Dog')

    def get_age(self):
        print("I am", self.age)
        
    def make_sound(self):
        print("Woof Woof")

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self,'Cat')

    def make_sound(self):
        print("Meow")

    def eating(self):
        print("The Cat is eating")
    
def main():
    if issubclass(Dog,Mammal):
        print("Dog is a subclass of Mammal")
        
    my_mammal = Mammal('Dog')
    my_dog = Dog('5')
    my_cat = Cat()

    if isinstance(my_mammal,Mammal):
        my_mammal.display_species()
        my_mammal.make_sound()
        
    print("---------")

    if isinstance(my_dog,Dog):
        my_dog.make_sound()
        my_dog.get_age()
        my_dog.display_species()
        
    print("---------")

    if isinstance(my_cat,Cat):
        my_cat.make_sound()
        my_cat.eating()
        my_cat.display_species()
    

if __name__ == '__main__':
    main()
