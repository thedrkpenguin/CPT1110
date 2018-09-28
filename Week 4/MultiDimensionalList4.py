MULTI_FLOOR_THEATER = []
#inner loop ("-"....) creats a row of 5 dashes
#outer loop (for j in...) does the above 4 times
#outer outer loop (for i in range(2))..... does the above 2 times

for f in range(2):  #floor in the theater
        row = [["-" for s in range(5)] for r in range(4)]
        MULTI_FLOOR_THEATER.append(row)

#print(MULTI_FLOOR_THEATER[0])
#print(MULTI_FLOOR_THEATER[1])

#print(MULTI_FLOOR_THEATER[0][0])
#print(MULTI_FLOOR_THEATER[0][0][0])


#MULTI_FLOOR_THEATER = [[["-" for s in range(5)] for r in range(4)] for f in range(2)]
floor = 1 
row = 2
seat = 2

MULTI_FLOOR_THEATER[floor][row][seat] = 'v' #second floor, 3rd row, 3rd seat
#MULTI_FLOOR_THEATER[1][2][2] = 'v'
#print(MULTI_FLOOR_THEATER[1])

MULTI_FLOOR_THEATER[0][0][4] = 'w' # first floor first row first seat
MULTI_FLOOR_THEATER[1][0][4] = 'x' # second floor first row first seat
MULTI_FLOOR_THEATER[0][3][0] = 'y' # first floor third row first seat
MULTI_FLOOR_THEATER[1][3][4] = 'z' # second floor third row fifth seat

#print(MULTI_FLOOR_THEATER)
#print(MULTI_FLOOR_THEATER[0])
#print(MULTI_FLOOR_THEATER[1])

for floor in MULTI_FLOOR_THEATER:
    for row in floor:
        for seat in row:
            print(seat, end="")
    print()
        

