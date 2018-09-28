FOOD = ["Pizza", "Burgers", "Fries", "Burgers","Ribs"]

print("Here is the current food menu: ")
print(FOOD)

FOOD_ITEM = str(input("Which item would you like to remove? "))

FOOD.remove(FOOD_ITEM)

print("Here is the new food menu: ")
print(FOOD)
