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
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)
            hero1.fight(hero2)
            if hero1.is_alive():
                living_opponents.remove(hero2)
            else:
                living_heroes.remove(hero1)

    def revive_heroes(self, health=100):
        for restore in self.heroes:
            restore.current_health = health

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{self.name} Kill/Deaths:{kd}")
            
    def remove_hero(self,name):
        remove_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                remove_hero = True
        if not remove_hero:
            return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)        

    def add_hero(self,hero):
        self.heroes.append(hero)