"""def zeroerrorfunction(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        print("Tried to divide by 0")
        raise
    #raise ZeroDivisionError
"""

def zeroerrorfunction(x):
    return 10 / x
try:
    zeroerrorfunction(0)
except ArithmeticError as err:
    #print("Arithmetic Error raised")
    print("Arithmetic Error: {0}".format(err))
except:
    print("What just happened?")

print("Program Terminated")
