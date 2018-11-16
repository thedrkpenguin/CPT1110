import empClass

def main():
    emp_name = str(input("Enter the employee name: "))
    id_number = str(input("Enter the employee id number: "))
    department = str(input("Enter the employee department name: "))
    job_title = str(input("Enter the employee job title: "))
    shift_number = str(input("Enter the employee shift number: "))
    pay_rate = str(input("Enter the employee pay rate: "))
    language = str(input("Enter the programming language: "))
    
    emp1 = empClass.Employee(emp_name,id_number,department,job_title,shift_number)
    emp2 = empClass.Employee("Bob Smith","2000","Marketing","Graphic Designer", "1")
    emp3 = empClass.Programmers(emp_name,id_number,department,job_title,shift_number,pay_rate,language)
    print("Employee Information")
    print("-" * 20)
    print(emp1)
    print()
    print(emp2)
    print()
    print(emp3)
    
if __name__ == "__main__":
    main()
