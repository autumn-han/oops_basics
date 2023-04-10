class BankAccount:
    bank_name = "Coding Dojo Credit Union"
    list_of_accounts = []
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate
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
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def display_user_balance(self):
        print(f"Balance: ${self.account.balance}")

autumn_han = User("Autumn", 28)
autumn_han.make_deposit(500).display_user_balance()