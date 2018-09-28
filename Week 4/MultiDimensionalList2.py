MY_2D_LIST = [[x for x in range(8)] for y in range(4)]

for row in MY_2D_LIST:
    for column in row:
        print(column, end="")
    print()

print(MY_2D_LIST)
