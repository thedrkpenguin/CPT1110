MOVIE_THEATER = []

#inner loop ("-"....) creats a row of 5 dashes
#outer loop (for i in...) does the above 4 times
#This builds the matrix to be referenced as row x column

for i in range(4): 
    row = ["-" for c in range(5)] 
    MOVIE_THEATER.append(row)
    print(MOVIE_THEATER) #shows the 2D list being constructed

#MOVIE_THEATER = [["-" for column in range(5)] for row in range(4)]

r = 0
c = 0
MOVIE_THEATER[r][c] = "x" # first row first seat

for i in range(1,4): 
    MOVIE_THEATER[2][i] = "x" # third row starting at seat 2 ending at seat 4

for i in range(0,5):
    MOVIE_THEATER[3][i] = "x" # forth row starting at seat 1 ending at seat 5

for i in range(0,3):
    MOVIE_THEATER[1][i] = "x"

for i in MOVIE_THEATER:
    for row in i:
        print(row, end="")
    print()
