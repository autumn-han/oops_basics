class BankAccount:
    bank_name = "Coding Dojo Credit Union"
    def __init__(self, account_name, balance, int_rate):
        self.account_name = account_name
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount): 
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount): 
        if self.balance < amount:
            print("Insufficient Funds: charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
        return self
    def display_account_info(self): 
        print(f"account name: {self.account_name}\nbalance: ${self.balance}\ninterest rate: {self.int_rate}")
    def yield_interest(self): 
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
    def create_account(self, account):
        self.dict_of_accounts[account.account_name] = f"balance - ${account.balance}, interest rate - {account.int_rate}"
    def make_deposit(self, account, amount):
        self.dict_of_accounts[account.account_name].deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"Balance: ${self.account.balance}")
    def display_all_accounts(self):
        print(f"{self.dict_of_accounts}")

autumn_han = User("Autumn", 28)
account1 = BankAccount("account1", 300, 0.02)
account2 = BankAccount("account2", 500, 0.04)
autumn_han.create_account(account1)
autumn_han.create_account(account2)
autumn_han.display_all_accounts()




