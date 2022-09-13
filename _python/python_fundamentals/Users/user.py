class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: " + self.name + " " + "Account Balance: " + str(self.account_balance))

    def transfer_money(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount


amin = User("Amin", 400)
amin.display_user_balance()
shatha = User("Shatha", 500)
shatha.display_user_balance()
sura = User("Sura", 300)
sura.display_user_balance()
#Have the first user make 3 deposits and 1 withdrawal and then display their balance
amin.make_deposit(100)
amin.make_deposit(80)
amin.make_deposit(60)
amin.make_withdrawal(200)
amin.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
shatha.make_deposit(200)
shatha.make_deposit(100)
shatha.make_withdrawal(50)
shatha.make_withdrawal(300)
shatha.display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
sura.make_deposit(300).make_withdrawal(120).make_withdrawal(50).make_withdrawal(100)
sura
sura.
sura.display_user_balance()

#Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
amin.transfer_money(sura,200)
amin.display_user_balance()
sura.display_user_balance()