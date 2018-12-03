import csv

csvfilename = "student_records.csv"

fields = []
rows = []

#with open("student_records.csv","r") as csvfile:
with open(csvfilename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    #fields = csvreader.next(csvfile) #Python 2.X
    fields = next(csvreader) #Python 3.x
    for r in csvreader:
        rows.append(r)
    print("Total number of rows is: ", csvreader.line_num)

print("Here are my fields: " + ', '.join(x for x in fields))
print()


for r in rows:
    for c in r:
        print(format(c,'10s'),end="")
    print('\n')
