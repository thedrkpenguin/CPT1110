#import math #imports all functions and must be qualified math.
#from math import * #imports all functions and no qualification
#from math import sin as sine, pi as pie
#import math as M

from math import sin,pi #imports only sin and pi and no qualification

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

#print(sin(pi/2))

pi = 3.14

#print(math.sin(math.pi/2))

print(sin(pi/2))
