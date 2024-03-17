"""
Scenario: Bank Account Operations
Imagine you're designing a banking application that allows users to perform various operations on their bank accounts, 
such as depositing money, withdrawing money, and transferring money between accounts. 
Users should also have the ability to undo their last operation if they make a mistake.

Requirements:
1 - Deposit Operation: Users can deposit a specified amount of money into their account. 
    This operation can be undone by withdrawing the same amount.

2 - Withdraw Operation: Users can withdraw a specified amount of money from their account if they have sufficient balance. 
    This operation can be undone by depositing the same amount back.

3 - Transfer Operation: Users can transfer a specified amount of money from one account to another if the source account has sufficient balance. 
    This operation can be undone by transferring the money back to the original account.

4 - Undo Functionality: After performing any of the above operations, users should have the option to undo the last operation. 
    This means the system needs to keep track of the operations history.
"""

from abc import ABC, abstractmethod
from typing import List


class User:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class BankAccount:

    def __init__(self, user: User) -> None:
        self.user = user
        self.balance = 0

    def deposite(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def __str__(self) -> str:
        return f"{self.user} with balance {self.balance}"


class BankingAction(ABC):

    @abstractmethod
    def execute(self, amount: float): ...

    @abstractmethod
    def undo(self): ...


class Withdrow(BankingAction):

    def __init__(self, back_account: BankAccount) -> None:
        self.back_account = back_account
        self.prev_balance = None
        self.withdrow_amount = None

    def execute(self, amount: float):
        self.prev_balance = self.back_account.balance
        self.withdrow_amount = amount
        self.back_account.withdraw(amount)

    def undo(self):
        if self.withdrow_amount:
            self.back_account.deposite(self.withdrow_amount)
        else:
            raise ValueError("you do not execute withdraw")


class Deposite(BankingAction):

    def __init__(self, back_account: BankAccount) -> None:
        self.back_account = back_account
        self.prev_balance = None
        self.deposite_amount = None

    def execute(self, amount: float):
        self.prev_balance = self.back_account.balance
        self.deposite_amount = amount
        self.back_account.deposite(amount)

    def undo(self):
        if self.deposite_amount:
            self.back_account.withdraw(self.deposite_amount)
        else:
            raise ValueError("you do not execute deposite")


class Transfer(BankingAction):

    def __init__(self, from_account: BankAccount, to_account: BankAccount) -> None:
        self.from_account = from_account
        self.to_account = to_account
        self.prev_from_account_balance = None
        self.prev_to_account_balance = None

    def execute(self, amount: float):
        self.prev_from_account_balance = self.from_account.balance
        self.prev_to_account_balance = self.to_account.balance
        self.amount = amount
        self.from_account.withdraw(self.amount)
        self.to_account.deposite(self.amount)

    def undo(self):
        if self.amount:
            self.from_account.deposite(self.amount)
            self.to_account.withdraw(self.amount)
        else:
            raise ValueError("you do not execute")


class BankingManager:

    def __init__(self) -> None:
        self.history: List[BankingAction] = []

    def execute(self, banking_action: BankingAction, amount: float):
        banking_action.execute(amount)
        self.history.append(banking_action)

    def undo(self):
        if self.history:
            blancking = self.history.pop()
            blancking.undo()


user = User(name="mousa nageh")
account = BankAccount(user=user)
deposite = Deposite(back_account=account)
withdrow = Withdrow(back_account=account)
banking = BankingManager()
banking.execute(banking_action=deposite, amount=200)
print(account.balance)  # 200
banking.execute(banking_action=withdrow, amount=100)
print(account.balance)  # 100
banking.undo()
print(account.balance)  # 200
banking.undo()
print(account.balance)  # 0
