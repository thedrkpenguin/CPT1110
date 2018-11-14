import random

class Coin():
    def __init__(self):
        self.sideup = "Tails" # can be passed to all methods in the class
        x = 5 #local variable inside this method only
        self.x = 5 # variable that can be passed to all methods in the clas
        
    def get_sideup(self): #method
        return self.sideup, self.x

    def toss(self): #method
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

def main(): #function
    my_coin = Coin() #create an object based on Coin class, instantiation

    print("The side of the coin currently showing is: ", my_coin.get_sideup())

    my_coin.toss()

    print("The side of the coin showing after the toss is: ", my_coin.get_sideup())

if __name__ == "__main__":
    main()
    

