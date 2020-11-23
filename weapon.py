import random
from ability import Ability

class Weapon(Ability):
    def __init__(self,name,max_damage=100):
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        random_value = random.randint(self.max_damage // 2,self.max_damage)
        return random_value

