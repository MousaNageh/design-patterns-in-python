'''
Scenario: Bank Account Operations with Undo/Redo Functionality

Originator (BankAccount): This is the class representing a bank account. 
It holds the balance of the account and has methods for performing operations like deposits and withdrawals.

Memento (BankAccountMemento): Objects of this class capture the state of a BankAccount object at a given time. 
The state here is the account balance. Each memento object is associated with a specific balance of the BankAccount.

Caretaker (BankAccountManager): This class manages the mementos created by the BankAccount.
It keeps a history of mementos representing the state changes of the bank account over time. It also implements the undo and redo functionalities by moving through this history and restoring the BankAccount's state from the mementos.
'''
from typing import List

class BankAccountMemento:
    
    def __init__(self, balance) -> None:
        self.balance = balance
    

class BankAccount:
    def __init__(self) -> None:
        self.balance = 0 
        self._states: List[BankAccountMemento]  = [BankAccountMemento(0)]
        self._current_state = 0
    
    def deposit(self, amount):
        self.balance +=amount
        self._states.append(BankAccountMemento(balance=self.balance))
        self._current_state +=1     
    
    def withdraw(self, amount):
        self.balance -= amount
        self._states.append(BankAccountMemento(balance=self.balance))
        self._current_state +=1     
    
    def undo(self):
        if self._current_state > 0:
            self._current_state -= 1
            self.balance  = self._states[self._current_state].balance 
        else:
            print("nothing too undo")
    
    def redo(self):
        if self._current_state < len(self._states)-1:
            self._current_state += 1 
            self.balance  = self._states[self._current_state].balance 
        else:
            print("nothing too redo")
    
    def display(self):  # Added method to display the current balance
        print(f"Current Balance: {self.balance}")


# Example usage
account = BankAccount()

account.deposit(100)
account.deposit(50)
account.display()  # Current Balance: 150

account.withdraw(20)
account.display()  # Current Balance: 130

account.undo()
account.display()  # Current Balance: 150

account.redo()
account.display()  # Current Balance: 130
            
        