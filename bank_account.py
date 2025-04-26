class BankAccount:
    def __init__(self, owner, balance=0.0):
        # Initialize a bank account with an owner and an initial balance.
        # Default balance is 0.0 if not specified.
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Deposit a positive amount into the account.
        # Raises a ValueError if the deposit amount is not positive.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        # Withdraw a specified amount from the account.
        # Raises a ValueError if the amount is negative or exceeds available balance.

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        # Returns the current balance of the account.
        return self.balance