import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    
    def __init__(self,name,starting_health=100):
        self.deaths = 0
        self.kills = 0
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def add_kill(self,num_kills):
        self.kills += num_kills

    def add_death(self,num_deaths):
        self.deaths += num_deaths

    def add_weapon(self,weapon):
        self.abilities.append(weapon)

    def add_ability(self,ability):
        self.abilities.append(ability)

    def add_armor(self,armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage_amt=0):
        total_block = 0
        for block in self.armors:
            total_block += block.block()
        return total_block

    def take_damage(self,damage=50):
        hurt = damage - self.defend(damage)
        self.current_health -= hurt

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if opponent.abilities and self.abilities:
            
            while self.current_health and opponent.current_health >= 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                
            if self.is_alive() or opponent.is_alive() == True:
                if self.is_alive() == False:
                    opponent.add_kill(1)
                    self.add_death(1)
                    print(f'{opponent.name} has won!')
                elif opponent.is_alive() == False:
                    self.add_kill(1)
                    opponent.add_death(1)   
                    print(f'{self.name} has won!')


