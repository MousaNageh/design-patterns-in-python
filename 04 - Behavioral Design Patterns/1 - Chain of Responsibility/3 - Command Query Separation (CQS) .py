"""
Command Query Separation (CQS) is a principle that suggests separating methods into two distinct categories: commands and queries.
Commands are responsible for performing actions, changing the state of the system, or the object, without returning any data.
Queries, on the other hand, are responsible for returning data to the caller, without changing the state of the system or the object.
This separation aims to make the system more understandable and maintainable.
"""


class Account:
    def __init__(self, balance=0):
        self._balance = balance

    # Command method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance is ${self._balance}.")
        else:
            print("Deposit amount must be positive.")

    # Command method
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self._balance}.")
        else:
            print(
                "Withdrawal amount must be positive and less than or equal to the balance."
            )

    # Query method
    def get_balance(self):
        return self._balance


"""
needed in broker chain
"""
