class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self): # have this method print all info on separate lines
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
    def enroll(self): # have this method change member status to True and award 200 card points
        if self.is_rewards_member == False: # BONUS: have the enroll method check the status of membership, before determining enrollment
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("ALERT: member is already enrolled")
    def spend_points(self, amount): # have this method deduct a given amount of points from the user
        if self.gold_card_points < amount: # BONUS: have this method be able to check overspending
            print("WARNING: you cannot spend more than your available gold card points")
        else:
            self.gold_card_points = self.gold_card_points - amount

autumn_han = User("Autumn", "Han", "autumn9894@gmail.com", "28") # first instance
autumn_han.display_info()
autumn_han.enroll()
autumn_han.display_info() # track the change from calling the enroll method

jane_doe = User("Jane", "Doe", "janedoe@gmail.com", "30") # second instance
billy_bob = User("Billy", "Bob", "billy.bob@gmail.com", "42") # third instance

# have the first user spend 50 points
autumn_han.spend_points(50)
#have the second user enroll, and then spend 80 points
jane_doe.enroll()
jane_doe.spend_points(80)
# call the display method on all users
autumn_han.display_info()
jane_doe.display_info()
billy_bob.display_info()




