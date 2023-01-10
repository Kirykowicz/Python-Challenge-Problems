from Animal import Animal 

class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)

    def bark(self):
        print(f"Woof! My name is {self.name}.")

    def who_am_i(self):
        print("I am a dog")

    def speak(self):
        return self.name + " says woof!"





