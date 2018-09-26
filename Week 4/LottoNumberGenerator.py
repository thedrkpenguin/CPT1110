import random

#LOTTERY_NUMBERS = [0] * 7

#for i in range(7):
#    LOTTERY_NUMBERS[i] = random.randint(0,9)

#print(LOTTERY_NUMBERS)

#for i in range(7):
#    print(LOTTERY_NUMBERS[i],end = '')
#
#    if i < 6:
#        print(', ', end = '')


LOTTERY_NUMBERS = []

for i in range(10):
    LOTTERY_NUMBERS.append(random.randint(0,9))

for i in range(10):
    print(LOTTERY_NUMBERS[i],end = '')

    if i < 9:
        print(', ', end = '')

