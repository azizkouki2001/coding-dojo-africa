class Bankacc:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance-5
        return self

    def display_acc_info(self):
        print("Balance: ",self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

def print_accs(accs):
    for acc in accs:
        acc.display_acc_info()

acc1 = Bankacc(0.02, 100)
acc2 = Bankacc()

acc1.deposit(50).deposit(100).deposit(200).withdraw(75).yield_interest().display_acc_info()
acc2.deposit(200).deposit(300).withdraw(100).withdraw(50).withdraw(25).withdraw(75).yield_interest().display_acc_info()

print_accs([acc1, acc2])