#import openpyxl (must be installed using pip)
import csv


fields = ["Name", "Divison", "Year", "GPA"]
rows = [["Kaelee", "AHS", "2019", "3.2"],["Paul", "BTPS", "2018", "3.0"], ["Xavier", "BTPS", "2020", "3.5"]]

with open("student_records.csv", "w",newline= "") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

