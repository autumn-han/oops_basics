import pet

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
    def nap_time(self):
        print("It's time for a nap for {}! Zzzzzz".format(self.pet.name))
        self.pet.sleep()
        return self

Chu = pet.Pet("Chu", "pika", "lightning", "peeeekah")
peter_tolly = Ninja("Peter", "Tolly", Chu, "broccoli", "tuna")

peter_tolly.walk().feed().bathe().nap_time()