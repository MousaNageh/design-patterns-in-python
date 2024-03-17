"""
The Composite Command, often associated with the Composite design pattern,
is a structural pattern used in the context of software development to treat both individual objects and compositions of objects uniformly. 
When applied to the Command pattern, it allows you to compose one or more commands into a single command object. 
This composite command then enables you to execute a batch of commands together,
treating them as a single operation. This approach is particularly useful when you want to implement macro commands or 
transactional operations that consist of multiple steps.
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


class CompositeBankingAction(BankingAction):

    def __init__(self) -> None:
        self.actions: List[BankingAction] = []

    def add_action(self, action: BankingAction):
        self.actions.append(action)

    def execute(self, amount: float):
        for action in self.actions:
            action.execute(amount)

    def undo(self):
        for action in reversed(self.actions):
            action.undo()


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
