from animal import Animal

class Dog(Animal):
    def __init__(self, name, breed, sleep_duration=12):
        self.sleep_duration = sleep_duration
        self.name = name
        self.breed = breed
        print("dog initialized!")
    def bark(self):
        print("Woof! Woof!")
    def sit(self):
        print("Sit!")
    def roll(self):
        print("Roll.")

my_dog = Dog("Sophie",12, 12)
my_dog.sleep()
my_dog.bark()
my_dog.eat()
my_dog.drink()