class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(Pet):
        pass
    def feed(self):
        pass
    def bathe(self):
        pass

class Pet:
    def __init__(self, name, type, tricks, sound, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print(self.sound)
