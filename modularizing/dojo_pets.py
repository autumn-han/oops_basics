class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet()
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
        print("Going for a walk with {}".format(self.pet.name))
    def feed(self):
        self.pet.eat()
        print("Feeding {} their favorite food, {}".format(self.pet.name, self.pet_food))
    def bathe(self):
        self.pet.noise()
        print("Oh no, it's time for a bath for {}".format(self.pet.name))

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
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.sound)
        return self

# make an instance of Ninja + assign them an instance of Pet to pet attribute
autumn_han = Ninja("Autumn", "Han", "dog", "bacon", "kibble")