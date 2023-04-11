class Player: # Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

