class BankAccount:
    bank_name = "Coding Dojo Credit Union"
    list_of_accounts = []
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.int_rate = 0.02
        self.__class__.list_of_accounts.append(self)
    @classmethod
    def display_all_info(cls):
        print(cls.list_of_accounts)
    def deposit(self, amount): # increases the account balance by the given amount
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount): # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance < amount:
            print("Insufficient Funds: charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
        return self
    def display_account_info(self): # print to the console: eg. "Balance: $100"
        print(f"First name: {self.first_name}\nLast name: {self.last_name}\nBalance: ${self.balance}")
    def yield_interest(self): # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance < 0:
            print("no interest rate")
        else:
            self.balance = self.balance * (1 + self.int_rate)
        return self

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self): # have this method print all info on separate lines
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
        return self # have methods able to chain to the user
    def enroll(self): # have this method change member status to True and award 200 card points
        if self.is_rewards_member == False: # BONUS: have the enroll method check the status of membership, before determining enrollment
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("ALERT: member is already enrolled")
        return self
    def spend_points(self, amount): # have this method deduct a given amount of points from the user
        if self.gold_card_points < amount: # BONUS: have this method be able to check overspending
            print("WARNING: you cannot spend more than your available gold card points")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self