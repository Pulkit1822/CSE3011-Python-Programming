class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("I am an animal!")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def __init__(self, name):
        super().__init__(name) # calling the super class constructor

d = Dog("Buddy")
d.make_sound()
d.name
