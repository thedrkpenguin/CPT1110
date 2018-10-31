def calc(x,y):
    try: 
        return x / y
    except ZeroDivisionError:
        return "You tried to divide by 0"
    except ArithmeticError:
        return "Can't divide by 0.  Second number must be > 0"
    
try:
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print(calc(x,y))
except (ValueError, KeyboardInterrupt):
    print("Must enter a number!")
except:
    print("I don't know what happened, but something bad did!")


#if y != 0:
#    print(calc(x,y))
#else:
#    print("Can't divide by 0")
    
