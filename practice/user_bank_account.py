class BankAccount:
    bank_name = "Coding Dojo Credit Union"
    def __init__(self, name, balance, int_rate):
        self.name = name
        self.balance = balance
        self.int_rate = int_rate
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
        self.dict_of_accounts = {}
    @classmethod
    def display_all_accounts(cls):
        print(cls.list_of_accounts)
    def create_account(self, account):
        self.dict_of_accounts[account.name] = account
    def make_deposit(self, account, amount):
        self.dict_of_accounts[account.name].deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"Balance: ${self.account.balance}")

autumn_han = User("Autumn", 28)

user = User()
account = BankAccount('name', 0.1, 100)
user.addAcc(account)
acc = user.dict_of_accounts['name']
user.make_withdrawal(acc, 100)
account = None

user.make_withdrawal('name', 100)

