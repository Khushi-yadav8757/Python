class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance
# Test
acc = BankAccount("Khushi", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.get_balance())
