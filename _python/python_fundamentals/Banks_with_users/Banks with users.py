class BankAccount:
  def __init__(self, int_rate = 0.001, balance = 0):
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f'your current balance: {self.balance}')
    return self

  def withdraw(self, amount):
    if amount < self.balance:
      self.balance -= amount
    else: print('insuffecient funds')
    return self
  def display_account_info(self):
    # your code here
    print(f'your current balance: {self.balance} and the interest rate is {self.int_rate}')
    return self
  def yield_interest(self):
    self.balance += (self.balance * self.int_rate)
    print(f'your current balance: {self.balance}')
    return self


acount_one = BankAccount(0.002, 100000)
acount_two = BankAccount(0.005, 1000000)

acount_one.deposit(100).deposit(1000).deposit(5000).withdraw(1000).display_account_info()
acount_two.deposit(10000).deposit(19922).withdraw(100).withdraw(1000).withdraw(190).withdraw(100).yield_interest().display_account_info()


class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = {}


  def deposit(self, amount, account_name):
    self.accounts[account_name].deposit(amount)
    print(self.accounts[account_name].balance)
    return self

  def withdraw(self, amount, account_name):
    self.accounts[account_name].withdraw(amount)
    return self

  def display_account_info(self, account_name):
    self.accounts[account_name].display_account_info()
    return self

  def yield_interest(self, account_name):
    self.accounts[account_name].yield_interest()
    return self

  def create_new_account(self, account_name, rate=0.02, balance=0):
    self.accounts[account_name] = BankAccount(rate, balance)
    print('account created successfully')



amin = User('Amin', 'amin.m.elayyan@email.com')
amin.create_new_account('arab-bank', 0.02, 0)
amin.create_new_account('bank-ahli', 0.2, 100)
amin.create_new_account('BOA', 0.2, 1200)
amin.deposit(100000, 'arab-bank')
amin.withdraw(1000, 'arab-bank')
amin.withdraw(1000, 'bank-ahli')
amin.display_account_info('bank-ahli')
amin.display_account_info('arab-bank')
amin.yield_interest('BOA')