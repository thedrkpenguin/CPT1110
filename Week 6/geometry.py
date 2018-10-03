import circle
import rectangle

def main():
    SELECTION = str(input("Calculate for a (c)ircle or (r)ectangle: "))

    if SELECTION == 'c':
        radius = int(input("Enter the radius of the circle: "))
        print("The area of the circle is: ",circle.area(radius))
        print("The circumference of the circle is: ",\
              circle.circumference(radius))

    if SELECTION == 'r':
        width = int(input("Enter the width of the rectangle: "))
        length = int(input("Enter the length of the rectangle: "))

        print("The area of the rectangle is: ",\
              rectangle.area(width=width,length=length)) 
        print("The perimeter of rectangle is: ",\
              rectangle.perimeter(width=width,length=length))

if __name__ == "__main__":
    main()

        
    
