class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = self.pi * radius**2 

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(3)

print(my_circle.get_circumference())

print(my_circle.area)
