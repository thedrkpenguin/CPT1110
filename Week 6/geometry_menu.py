import circle
import rectangle

AREA_CIRCLE = 1
CIRCUMFERENCE_CIRCLE = 2
AREA_RECTANGLE = 3
PERIMETER_RECTANGLE = 4
QUIT_CHOICE = 5

def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == AREA_CIRCLE:
            radius = float(input("Enter the radius of the circle: "))
            print("The area of the circle is ", circle.area(radius), "units")
            
        elif choice == CIRCUMFERENCE_CIRCLE:
            radius = float(input("Enter the radius of the circle: "))
            print("The circumference of the circle is ", circle.circumference(radius), "units")
            
        elif choice == AREA_RECTANGLE:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Ente the width of the rectangle: "))
            print("The area of the rectangle is ", rectangle.area(length, width), "units")
            
        elif choice == PERIMETER_RECTANGLE:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Ente the width of the rectangle: "))
            print("The perimeter of the rectangle is ", rectangle.perimeter(length, width), "units")
            
        elif choice == QUIT_CHOICE:
            print("Exiting the program.....")
        else:
            print("Error, you selected an invalid choice!!!")

def display_menu():
    print('  Menu  ')
    print('1 - Area of circle')
    print('2 - Circumference of circle')
    print('3 - Area of rectangle')
    print('4 - Perimeter of rectangle')
    print('5 - Quit')
    
if __name__ == "__main__":
    main()
