# r = float(input("enter the radius of circle : "))
# area = (22/7) * (r**2)
# print(area)


x = float(input("enter the radius of circle : "))
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self,radius):
        return (22/7)*(self.radius**2)
    
    def perimeter(self,radius):
        return (2)*(22/7)*(self.radius)

c1 = Circle(x)
c1_area = c1.area(x)
c1_perimeter = c1.perimeter(x)
print("the area of circle is =", c1_area)
print("the perimeter of circle =", c1_perimeter)