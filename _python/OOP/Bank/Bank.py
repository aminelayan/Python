class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.int_rate = 0.05
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance<amount:
                print("Insufficient funds: Charging a $5 fee and deduct $5")
                self.balance-=5
        else: self.balance -= amount
        return self
    def display_account_info(self):
        print("account number:",self.account_number,"intereset rate: ",self.int_rate,"account balance: ",self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance*self.int_rate)
        else:
            self.balance += 0
        return self

n111 =BankAccount(778,2000)
n112 =BankAccount(753,2500)

 # To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
n111.withdraw(2800).yield_interest().display_account_info()

 # To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
n112.deposit(400).deposit(100).withdraw(200).withdraw(100).withdraw(50).yield_interest().display_account_info()



#meshan allah 3lmne el code ):