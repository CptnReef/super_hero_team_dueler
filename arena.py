from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")
    
    def create_ability(self):
        name = input("What is the ability name?")
        max_damage = input("What is the max damage of the ability?")

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?")
        max_damage = input("What is the max damage of the weapon?")

        return Weapon(name, max_damage)
    
    def create_armor(self):
        name = input("What is the block name?")
        max_block = input("What is the max block of the armor?")

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero() 
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero() 
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print(self.team_one.name + " statistic: \n")
        self.team_one.stats()
        print(self.team_two.name + " statistic: \n")
        self.team_two.stats()

        team_kills = 0
        team_deaths = 0

        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            teams_deaths = 1
        print(self.team_one.name + " averag k/d was: " + str(team_kills/teams_deaths))

        teams_kills = 0
        team_deaths = 0

        for hero in self.team_two.heroes:
            teams_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            teams_deaths = 1
        print(self.team_two.name + " averag k/d was: " + str(team_kills/teams_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print(f"survived from {self.team_one.name}: {hero.name}")

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print(f"survived from {self.team_two.name}: {hero.name}")



if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()