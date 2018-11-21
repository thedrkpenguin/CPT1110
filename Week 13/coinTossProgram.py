import random

class Coin():
    def __init__(self):
        self.__sideup = "Tails" # can be passed to all methods in the class
            
    def get_sideup(self): #method
        return self.__sideup

    def toss(self): #method
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

def main(): #function
    my_coin = Coin() #create an object based on Coin class, instantiation

    print("The side of the coin currently showing is: ", my_coin.get_sideup())

    my_coin.toss()

    my_coin.__sideup = "Hacked Coin" #because the variable is public

    print("The side of the coin showing after the toss is: ", my_coin.get_sideup())

if __name__ == "__main__":
    main()
    

