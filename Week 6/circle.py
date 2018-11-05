import math

def area(radius):
    return math.pi * (radius ** 2)

def circumference(radius):
    return 2 * math.pi * radius

if __name__ == "__main__":
    print("This is circle running normal")
else:
    print("This is circle being imported")
