def EXPLOSION(explode = True):
    print("Three.....")
    print("Two.....")
    print("One.....")
    if not explode:
        return
    print("BOOM!!!!")

EXPLOSION()

def FUNCTION_1(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(FUNCTION_1(4))
print(FUNCTION_1(5))
