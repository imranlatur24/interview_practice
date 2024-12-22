class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

# Create a bank account object
account = BankAccount("1234567890", 1000)

# Get account information using the interface methods
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())

# Attempt to withdraw more money than available
account.withdraw(2000)

# Deposit some money and try again
account.deposit(500)
account.withdraw(2000)
print("Balance:", account.get_balance())
