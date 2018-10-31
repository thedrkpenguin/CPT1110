import math

def main():
    try:
        AGAIN = 'y'
        while AGAIN == 'y':
            x = float(input("Enter a number: "))
            assert x >= 0 # this replaces the if/else
            x = math.sqrt(x)
            print(x)
            AGAIN = str(input("Would you like to continue? "))
    except AssertionError:
        print("number not greater than 0")
        main()
    
main()


#if x >= 0:
#    x = math.sqrt(x)
#else:
#    print("number must be greater than 0")




