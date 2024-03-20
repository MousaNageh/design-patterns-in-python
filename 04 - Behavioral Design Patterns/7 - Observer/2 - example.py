'''
Scenario: Stock Market Alert System
Objective: Develop a system that allows users to subscribe to alerts for specific stock price changes.
When a stock's price reaches a certain threshold, all subscribed users should be notified.
'''
from typing import  Callable, List

class Observable:
    
    def __init__(self) -> None:
        self._observers: List[Callable] = []
    
    def add_observer(self, observer: Callable):
        self._observers.append(observer)  
    
    def remove_observer(self, observer: Callable):
        self._observers.remove(observer)
    
    def notify_observers(self, *args, **kwds):
        for observer in self._observers:
            observer(*args, **kwds)        
          
    

class User:
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def notify(self, message: str):
        print(f"{self.name} received notification: {message}")

class Stock:
    
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self._price = price
        self.observable: Observable = Observable()
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value: float):
        old_price = self._price
        self._price = value
        self.observable.notify_observers(self.name, old_price, self._price)


class StockAlert:
    
    def __init__(self, user: User, stock: Stock, threshold: float) -> None:
        self.user = user
        self.stock = stock
        self.threshold = threshold
        # Register this StockAlert as an observer to the stock
        self.stock.observable.add_observer(self.check_price)
    
    def check_price(self, stock_name: str, old_price: float, new_price: float):
        if (old_price < self.threshold <= new_price) or (old_price > self.threshold >= new_price):
            self.user.notify(f"Stock {stock_name} crossed your threshold of {self.threshold}. New price: {new_price}")
    
    def unsubscribe(self):
        self.stock.observable.remove_observer(self.check_price)


user1 = User(name='Mousa')
user2 = User(name='Nora')

apple_stock = Stock(name='Apple', price=100)
# Users subscribe to Apple stock alerts for different price thresholds
alert1 = StockAlert(user1, apple_stock, 150)
alert2 = StockAlert(user2, apple_stock, 90)

# Simulate price changes
apple_stock.price = 200  # Mousa will be notified
apple_stock.price = 85   # Nora will be notified


        
        
