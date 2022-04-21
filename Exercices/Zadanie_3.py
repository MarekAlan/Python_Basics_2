class BankAccount:
    def __init__(self, account_number):
        self.acc = account_number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if amount < 0:  #jeżeli jest ujemne to kończymy
            return
        if amount > self.cash:
            amount = self.cash
        self.cash -= amount
        return amount

    def print_info(self):
        print(f'Stan konta o numerze {self.acc} to {self.cash} forintów')

konto = BankAccount('56478382')
print(konto.acc)
print(konto.cash)

konto.deposit_cash(200)
print(konto.withdraw_cash(150))

konto.print_info()


