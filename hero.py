import random
from ability import Ability
from armor import Armor

class Hero:
    
    def __init__(self,name,starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

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
                if self.is_alive() == True:
                    print(f'{self.name} has won!')
                    break
                else:
                    print(f'{opponent.name} has won!')
                    break
        else:
            print('Draw')

  # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
  # 3) After each attack, check if either the hero (self) or the opponent is alive
  # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 380)
    ability4 = Ability("Wizard Beard", 320)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
