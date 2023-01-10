from Animal import Animal

class Cat(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return self.name + " says meow"