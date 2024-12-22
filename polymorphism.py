class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def make_sound():
        pass

class Dog(Animal):
    def make_sound(self):
        return "woaf!"

class Cat(Animal):
    def make_sound(self):
        return "meow!"

animals = [Dog('Woalfy'),Cat('Kitty')]
for animal in animals:
    print(f'{animal.name} says {animal.make_sound()}')