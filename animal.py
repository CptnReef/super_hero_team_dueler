class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(f"{self.name} sleeps for {self.sleep_duration} hours.")

    def eat(self):
        print(f"{self.name} is eating!")

    def drink(self):
        print(f"Thirsty {self.name} is drinking!")

class Frog(Animal):
    def __init__(self, name):
        self.name = name
        print("Riiiiibit!")

    def jump(self):
        print(f"{self.name} is jumping!")

Froggy = Frog("Frogger")

Froggy.eat()
Froggy.drink()
Froggy.jump()
