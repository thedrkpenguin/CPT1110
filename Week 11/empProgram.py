import empClass

def main():
    emp_name = str(input("Enter the employee name: "))
    id_number = str(input("Enter the employee id number: "))
    department = str(input("Enter the employee department name: "))
    job_title = str(input("Enter the employee job title: "))
    shift_number = str(input("Enter the employee shift number: "))

    emp1 = empClass.Employee(emp_name,id_number,department,job_title,shift_number)
    emp2 = empClass.Employee("Bob Smith","2000","Marketing","Graphic Designer", "1")
    emp3 = empClass.Employee("Steve Rogers","3000","IT","Help Desk", "2")
    
    print("Employee Information")
    print("-" * 20)
    print(emp1)
    print()
    print(emp2)
    print()
    print(emp3)
    print("-" * 20)
    
    emp1.change_id_number("31337")
    print(emp1)

    print(empClass.Employee.__dict__)
    
    """
    print("Employee Name: ",emp1.display_name())
    print("ID Number: ",emp1.display_id_number())
    print("Department: ",emp1.display_department())
    print("Job Title: ",emp1.display_job_title())
    print("Shift Number: ",emp1.display_shift_number())

    print("Employee Name: ",emp2.display_name())
    print("ID Number: ",emp2.display_id_number())
    print("Department: ",emp2.display_department())
    print("Job Title: ",emp2.display_job_title())
    print("Shift Number: ",emp2.display_shift_number())
    """

if __name__ == "__main__":
    main()
