class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        print("Going for a walk with {}".format(self.pet.name))
        self.pet.play()
        return self
    def feed(self):
        print("Feeding {} their favorite food, {}".format(self.pet.name, self.pet_food))
        self.pet.eat()
        return self
    def bathe(self):
        print("Oh no, it's time for a bath for {}".format(self.pet.name))
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 0
        self.energy = 0
    def sleep(self):
        self.energy += 25
        print("{}'s energy increased by 25 points! Now their energy is at {}".format(self.name, self.energy))
    def eat(self):
        self.energy += 5
        self.health += 10
        print("{}'s energy went up by 5 points and their health by 10 points! Now their energy is at {} and their health is at {}".format(self.name, self.energy, self.health))
    def play(self):
        self.health += 5
        print("{}'s health went up by 5 points! Now their health is at {}".format(self.name, self.health))
    def noise(self):
        print(self.sound)

# make an instance of Ninja + assign them an instance of Pet to pet attribute
Roo = Pet("Roo", "dog", "shake", "bark bark!")
autumn_han = Ninja("Autumn", "Han", Roo, "bacon", "kibble")
autumn_han.walk().feed().bathe()