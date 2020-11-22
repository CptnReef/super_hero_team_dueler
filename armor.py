import random

class Armor:
    def __init__(self,name,max_block=10):
        self.name = name
        self.max_block = max_block

    def block(self):
        self.random_value = random.randint(0,self.max_block)
        return self.random_value

