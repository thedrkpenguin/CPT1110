import csv

mydict =[{'Division': 'BTPS', 'Gpa': '3.0', 'Name': 'Paul', 'Year': '2018'}, 
         {'Division': 'AHS', 'Gpa': '3.1', 'Name': 'Kaelee', 'Year': '2019'}, 
         {'Division': 'BTPS', 'Gpa': '3.3', 'Name': 'Xavier', 'Year': '2020'}] 
  
# field names 
fields = ['Name', 'Division', 'Year', 'Gpa'] 
  
# name of csv file 
filename = "student_records_dict.csv"
  
# writing to csv file 
with open(filename, 'w',newline="") as csvfile:
#with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
      
    # writing headers (field names) 
    writer.writeheader() 
      
    # writing data rows 
    writer.writerows(mydict) 
