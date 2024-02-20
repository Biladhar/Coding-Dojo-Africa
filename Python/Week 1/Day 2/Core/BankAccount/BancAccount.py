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



account1 = BankAccount(0.01,100)
account2 = BankAccount(0.01,200)

account1.deposit(50).deposit(50).deposit(500).withdraw(250).yield_interest().display_account_info()
print("="*30)
account2.deposit(1000).deposit(1500).withdraw(750).withdraw(50).withdraw(200).withdraw(300).yield_interest().display_account_info()
print("="*30)
BankAccount.all_account_info()