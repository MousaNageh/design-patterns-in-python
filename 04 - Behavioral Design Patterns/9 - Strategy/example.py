
from abc import ABC, abstractmethod 

class TaxCalculationStrategy(ABC):
    
    @abstractmethod
    def get_tax(self, amount: float): ...

class USTaxStrategy(TaxCalculationStrategy):
    
    def get_tax(self, amount: float):
        return amount + amount * .3 
    


class CanadaTaxStrategy(TaxCalculationStrategy):
    
    def get_tax(self, amount: float):
        return amount + amount * .24


class EUTaxStrategy(TaxCalculationStrategy):
    
    def get_tax(self, amount: float):
        return amount + amount * .4


class Account:
    def __init__(self, balance: float):
        self.balance = balance


class Tax:
    
    def __init__(self, acount: Account, tax: TaxCalculationStrategy) -> None:
        self.account = acount
        self.tax = tax
        
    def get_balance_with_tax(self):
        return self.tax.get_tax(self.account.balance)