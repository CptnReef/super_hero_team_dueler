import random
class Hero():
    
    def __init__(self,name,starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        self.opponent = Hero(opponent)
        
        if self.opponent:
            self.current_health -= random.randint(1,100)
            if self.current_health <= 50:
                print(f'{self.opponent.name} is Winner!')
            else:
                print(f'{self.name} won the battle!')
            
                



if __name__ == "__main__":
    my_hero = Hero("Grace Hopper")
    my_opponent = Hero("Black Widow")

    my_hero.fight("Wonder Woman")
    my_opponent.fight("Dumbledore")
