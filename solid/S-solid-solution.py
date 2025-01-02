import datetime

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

class Deposit:
    def __init__(self, account: BankAccount):
        self.account = account
        
    def deposit(self, account: BankAccount, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account.balance += amount

        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Deposited {amount} into {self.account.account_number}\n"
            )

        print(f"Sending email notification: {amount} deposited into account {self.account.account_number}.")

class Withdraw:
    def __init__(self, account: BankAccount):
        self.account = account

    def withdraw(self, amount, account: BankAccount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.account.balance -= amount

        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Withdrew {amount} from {self.account.account_number}\n"
            )

        print(f"Sending email notification: {amount} withdrawn from account {self.account.account_number}.")

class GenerateAccount:
    def __init__(self, account: BankAccount):
        self.account = account

    def generate_statement(self):
        statement = f"Statement for Account: {self.account.account_number}\nBalance: {self.account.balance}\n"

        print(statement)

        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {self.account.account_number}\n"
            )
        print(f"Sending email with statement for account {self.acoount.account_number}...")