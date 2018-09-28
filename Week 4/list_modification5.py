FOOD = ["Pizza", "Burgers", "Fries", "Ribs"]

print("Here is the current food menu: ")
print(FOOD)

FIRST_FOOD_ITEM = str(input("First item to swap: "))
SECOND_FOOD_ITEM = str(input("Second item to swap: "))

FIRST_ITEM_INDEX = FOOD.index(FIRST_FOOD_ITEM)
SECOND_ITEM_INDEX = FOOD.index(SECOND_FOOD_ITEM)

FOOD[FIRST_ITEM_INDEX],FOOD[SECOND_ITEM_INDEX] = FOOD[SECOND_ITEM_INDEX], \
                                                 FOOD[FIRST_ITEM_INDEX]

print("Here is the altered food menu: ")
print(FOOD)
