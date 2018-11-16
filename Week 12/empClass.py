class Employee():
    def __init__(self,name,id_number,department,job_title,shift_number):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.shift_number = shift_number

    def display_name(self):  #accessor method
        return self.name

    def display_id_number(self): #accessor method
        return self.id_number

    def display_department(self): #accessor method
        return self.department

    def display_job_title(self): #accessor method
        return self.job_title

    def display_shift_number(self): #accessor method
        return self.shift_number

    def change_id_number(self,id_number): #mutator method
        self.id_number = id_number

    def __str__(self): #executed automatically when the print() function
                       #is called.  print(object_name)
        information = 'Name: ' + self.display_name() + '\nID Number: ' +\
                      self.display_id_number() +'\nDepartment: ' + \
                      self.display_department() + '\nJob Title: ' + \
                      self.display_job_title() + '\nShift Number: ' + \
                      self.display_shift_number()
        return information

class Programmers(Employee):
    def __init__(self,name,id_number,department,job_title,shift_number,pay_rate,language):
        Employee.__init__(self,name,id_number,department,job_title,shift_number)
        self.pay_rate = pay_rate
        self.language = language

    def display_pay_rate(self):
        return self.pay_rate

    def display_language(self):
        return self.language

    def __str__(self): #executed automatically when the print() function
                       #is called.  print(object_name)
        information = 'Name: ' + self.display_name() + '\nID Number: ' +\
                      self.display_id_number() +'\nPay Rate: ' + \
                      self.display_pay_rate() + '\nLanguage: ' + \
                      self.display_language()
        
        return information
