from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdralTimeRestictionError

class BankAccount:
    def __init__(self, balance=0, log_file = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposits cannot be negative")
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        now = datetime.now()
        if now.hour <8 or now.hour > 17:
            raise WithdralTimeRestictionError("Withdrawl are only available from 8AM to 5PM")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Withdral of {amount} exceeds your balance: {self.balance}"
            )

        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdraw {amount}. New balance: {self.balance}")

        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance
    