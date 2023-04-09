class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount): # increases the account balance by the given amount
        self.balance = self.balance + amount
    def withdraw(self, amount): # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance < amount:
            print("Insufficient Funds: charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
    def display_account_info(self): # print to the console: eg. "Balance: $100"
        print(f"Balance: ${self.balance}")
    def yield_interest(self): # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance < 0:
            print("no interest rate")
        else:
            self.balance = self.balance * 1.04