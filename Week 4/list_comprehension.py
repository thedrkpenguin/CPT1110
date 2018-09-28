# [expression for item in list if conditional]

NUMBER_LIST = [ x for x in range(10)]
print("Number list below: ")
print(NUMBER_LIST)

SQUARES_LIST = [ x ** 2 for x in range(10)]
print("List of squares below: ")
print(SQUARES_LIST)

LtoH = [x.upper() for x in ['a', 'b', 'c']]
print("Convert to Upper: ")
print(LtoH)

HtoL = [x.lower() for x in ['A', 'B', 'C']]
print("Convert to Lower: ")
print(HtoL)
        
NO_PRIMES = [ x for y in range(2,10) for x in range(y*2, 10, y)]
print("No Prime Numbers: ")
print(NO_PRIMES)
        
MY_PRIMES = [x for x in range(2,10) if x not in NO_PRIMES]
print("My Primes: ")
print(MY_PRIMES)
        
PRIMES = [p for p in range(2,10) if 0 not in [ p % d for d in range(2,p)]]
print("More Primes: ")
print(PRIMES)
