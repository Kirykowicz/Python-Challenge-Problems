import math

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)

    def slope(self):
        return ((self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0]))

new_line = Line((1,2), (3,4))
print(new_line.distance())
print(new_line.slope())

class Cylinder:

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.height * self.radius**2

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)


c = Cylinder(2,3)

print(str(c.volume()) + " is the volume")

print(str(c.surface_area()) + " is the surface area")