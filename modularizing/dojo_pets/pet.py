class Pet:
    def __init__(self, name, tricks, sound):
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

# use inheritance to make a sub-class of the Pet class
class Dog(Pet):
    def __init__(self, name, tricks, sound):
        super().__init__(name, tricks, sound)
        self.health = 10
        self.energy = 10
    def throw_ball(self):
        print("You threw the ball and {} ran after it!".format(self.name))
        super().play()
        return self
    def offer_treat(self):
        print("You offer {} a treat, and they {}".format(self.name, self.tricks))
        super().eat()
        return self
    def scratch_ear(self):
        print("You scratch {} behind the ear, and she happily leans into your hand".format(self.name))
        super().noise()
    def play_music(self):
        print("You play music for {}, and they sleepily close their eyes, lower their muzzle, and doze off".format(self.name))
        super().sleep()
        return self

Ferna = Dog("Ferna", "sit", "woof woof!")
Ferna.throw_ball().offer_treat().play_music()
