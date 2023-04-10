class BankAccount:
    bank_name = "Coding Dojo Credit Union"
    list_of_accounts = []
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
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
            self.balance = self.balance * 1.05
        return self

# create two accounts
autumn_han = BankAccount("Autumn", "Han", 800)
joey_wheeler = BankAccount("Joey", "Wheeler", 750)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
autumn_han.deposit(30).deposit(45).deposit(20).withdraw(200).yield_interest().display_account_info()
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
joey_wheeler.deposit(100).deposit(50).withdraw(400).yield_interest().display_account_info()

BankAccount.display_all_info()