import math

class Circle:
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
r = float(input('\nEnter the radius of the circle:  '))

c=Circle(r)

print('\nArea:  ',c.area(),)
print('Perimeter:  ',c.perimeter(),'\n')