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

