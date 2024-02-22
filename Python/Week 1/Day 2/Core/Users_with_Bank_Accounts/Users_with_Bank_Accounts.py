class BankAccount:
    all_account = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_account.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        charging = 5
        if(self.balance>=amount):
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        
    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
    def yield_interest(self):
        if (self.balance>0):
            interest = self.balance * self.int_rate
            self.balance += interest
            return self
    @classmethod
    def all_account_info(cls):
        for account in cls.all_account:
            account.display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.balance += amount
    def make_withdrawal(self, amount):
        self.account.balance -= amount
    def display_user_balance (self):
        self.account.display_account_info()

user1 = User("bilel","a@a.a")
user1.make_deposit(1000)
user1.make_withdrawal(500)
user1.display_user_balance()



