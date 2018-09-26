PRIMES = []
USER_NUMBER = int(input("Enter a number: "))

for x in range(2,USER_NUMBER + 1):
    for y in range(2,x):
        if x % y == 0:
            break
    else:
        PRIMES.append(x)
        
print(PRIMES)


PRIMES = [x for x in range(2,101) if all(x % y !=0 for y in range(2,x))]

print(PRIMES)



        
        
