class Dog:
    def __init__(self, name):
        self.name = name
        print("dog initialized!")

my_dog = Dog("Rex")
print(my_dog)
print(my_dog.name)
print('-------------------------------')
my_dog.breed = "SuperDog"
print(my_dog.breed)