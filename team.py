import random
from hero import Hero

class Team:
    
    def __init__(self,name):
        self.name = name
        self.heroes = list()

    def attack(self, other_team):

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            living_heroes.append(hero.fight(random.choice(living_heroes)))
            living_opponents.append(hero.fight(random.choice(living_opponents)))

    def revive_heroes(self, health=100):
        self.current_health = health

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{self.name} Kill/Deaths:{kd}")
            
    def remove_hero(self,name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
            if not foundHero:
                return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            return print(hero)        

    def add_hero(self,hero):
        self.heroes.append()