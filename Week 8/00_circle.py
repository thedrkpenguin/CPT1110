import math

def area(radius):
    return math.pi * (radius ** 2)

def circumference(radius):
    return 2 * math.pi * radius

if __name__ == "__main__":
    print("I am " ,__name__)
    print("I am not being imported")
else:
    print("I am circle and I am imported as ", __name__)

    
