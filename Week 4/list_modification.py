NAME_LIST = []

AGAIN = 'y'

while AGAIN == 'y' or AGAIN == 'Y':
    NAME = str(input("Enter a name: "))

    NAME_LIST.append(NAME)

    print("Do you want to enter another name?")
    AGAIN = str(input("y = yes, n = no: "))


print("Below are the names in the list: ")
for item in NAME_LIST:
    print(item)
