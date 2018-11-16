for i in range(1,3): #outermost loop
    print('Current value for i is: ', i)
    for x in reversed(range(0,10)): #innermost loop
        if x == 5:
            continue
            #break
        print('Current value for x is: ', x)


