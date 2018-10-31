def zeroerrorfunction(x):
    #return 10 / x
    raise ZeroDivisionError
def anotherfunction(x):
    #return 10/x
    raise ZeroDivisionError
    
try:
    zeroerrorfunction(0)
except ArithmeticError:
    print("Arithmetic Error raised")
except ZeroDivisionError:
    print("Zero Division")
except:
    print("What just happened?")

try:
    anotherfunction(0)
except ZeroDivisionError:
    print("This is from another function: ZeroDivisionError")
    

print("Program Terminated")
