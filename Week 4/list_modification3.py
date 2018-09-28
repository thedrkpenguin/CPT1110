FOOD = ["Pizza", "Burgers", "Fries", "Ribs"]

print("Here is the current food menu: ")
print(FOOD)

FOOD_ITEM = str(input("Which item would you like to insert? "))

FOOD.insert(2, FOOD_ITEM)

print("Here is the new food menu: ")
print(FOOD)
