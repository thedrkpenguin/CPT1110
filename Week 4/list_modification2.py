FOOD = ["Pizza", "Burgers", "Fries", "Ribs"]

print("Here is the current food menu: ")
print(FOOD)

FOOD_ITEM = str(input("Which item would you like to change? "))
#Fries --> index value 2

ITEM_INDEX = FOOD.index(FOOD_ITEM)
#ITEM_INDEX = 2

NEW_ITEM = str(input("Enter the new food item: "))
#NEW_ITEM = Steak

FOOD[ITEM_INDEX] = NEW_ITEM
#FOOD[2] = STEAK


print("Here is the new food menu: ")
print(FOOD)
