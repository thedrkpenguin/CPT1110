class Point():
    def __init__(self,x,y):
        self.x = x #self.x = 6
        self.y = y #self.y = 8

    def distance(self):
        return (self.x**2 + self.y**2) ** .5 #pythagorean theorum
    
    #def distance(self,x=0,y=0):
        #return (x**2 + y**2) ** .5 #pythagorean theorum
        
first_point = Point(6,8) #send 6 as first parameter, 8 as the second
second_point = Point(12,20) #send 12 as first parameter, 20 as the second

x = int(input("Enter a x-coordinate: "))
y = int(input("Enter a y-coordinate: "))

third_point = Point(x,y)

print("The distance (first point) of this point from the origin is: "\
      , first_point.distance())

print("The distance (second point) of this point from the origin is: "\
      , second_point.distance())

print("The distance (third point) of this point from the origin is: "\
      , third_point.distance())


#print("The distance of this point from the origin is: "\
#      , Point.distance(first_point))

#print("This is with the class name first: ", type(Point.distance))
#print("This is with the objects name first: ", type(first_point.distance))


        
