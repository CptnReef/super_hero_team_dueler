import random

class Weapon:
    def __init__(self,name,max_damage=100):
        self.name = name
        self.max_damage = max_damage * 0.5
    
    def attack(self):
        random_value = random.randint(0,self.max_damage)
        return random_value

