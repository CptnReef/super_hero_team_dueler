import random

class Ability:
    def __init__(self,name,max_damage=100):
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        self.random_value = random.randint(0,self.max_damage)
        return self.random_value

