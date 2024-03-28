'''

The Strategy Design Pattern is a behavioral design pattern that enables selecting an algorithm's behavior at runtime. 
Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.
'''

'''
Scenario: Discount Strategy for an E-commerce Platform
Imagine you're developing an e-commerce platform. The platform offers various types of discounts based on different criteria:
a discount for festive seasons,
a discount for clearance sales, 
and a loyalty discount for regular customers.
Instead of hardcoding each discount into the order processing system, you use the Strategy pattern. 
This approach allows for dynamically changing the discount strategy based on the sale type or customer without altering the system's core logic.
'''
from abc import ABC, abstractmethod

# Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_value):
        pass
    

# Concrete Strategy 1
class FestiveDiscountStrategy(DiscountStrategy):
    def apply_discount(self, order_value):
        return order_value * 0.9  # 10% discount

# Concrete Strategy 2
class ClearanceDiscountStrategy(DiscountStrategy):
    def apply_discount(self, order_value):
        return order_value * 0.8  # 20% discount

# Concrete Strategy 3
class LoyaltyDiscountStrategy(DiscountStrategy):
    def apply_discount(self, order_value):
        return order_value * 0.85  # 15% discount
    

# Context Class
class Order:
    def __init__(self, customer, total, discount_strategy: DiscountStrategy =None):
        self.customer = customer
        self.total = total
        self.discount_strategy = discount_strategy

    def apply_discount(self):
        if self.discount_strategy:
            self.total = self.discount_strategy.apply_discount(self.total)
        return self.total