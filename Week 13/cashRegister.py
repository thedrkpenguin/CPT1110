# Programming Exercise 10-7

import retail

class CashRegister:

    # Initialize an empty list to hold purchased items.
    def __init__(self):

        self.__items = []

    # Method that clears the contents of the cash register.
    def clear(self):

        self.__items = []

    # Method that simulates adding an item to the cash register.
    # Receives a RetailItem object as an argument. 
    def purchase_item(self, retail_item):

        self.__items.append(retail_item)
        print('The item was added to the cash register.')

    # Method returning the total cost of items at the cash register.
    def get_total(self):

        total = 0.0
        for item in self.__items:
            total = total + item.get_price()

        return total

    # Method that prints a list of items at the cash register.
    def show_items(self):

        print('The items in the cash register are:')
        print()
        for item in self.__items:
            print(item)
            print()



