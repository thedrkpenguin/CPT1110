for i in range(4):
    for j in range(4):
        if j == 3:
            break
        print(i,j)
        
COUNTER = 0
while True:
    number = int(input("Enter a number: "))

    if number == 5:
        break
    COUNTER += 1

print(COUNTER)
    
