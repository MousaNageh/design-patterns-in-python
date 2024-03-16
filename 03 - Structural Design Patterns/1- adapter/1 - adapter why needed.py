"""
The Adapter Design Pattern is a structural design pattern. 
It allows objects with incompatible interfaces to collaborate. 
The main purpose of this pattern is to create a bridge between two incompatible interfaces by creating an adapter class.
This adapter class implements the interface of one of the objects and wraps the other object, 
so it can use its services albeit through the adapter's interface.


Here are the key components of the Adapter Pattern:

1 - Target: The interface that the client expects or wants to use.

2 - Adaptee: The class that needs to be adapted. This class contains some useful behavior, but its interface is incompatible with the client.

3 - Adapter: The class that implements the Target interface and contains an instance of Adaptee. 
             It translates calls to the Target interface into calls to the Adaptee's interface.
"""

from abc import ABC, abstractmethod


# Adaptee 1
class PayPal:
    def send_payment(self, amount):
        print(f"PayPal: Processing payment of {amount}")


# Adaptee 1
class Stripe:
    def make_payment(self, amount):
        print(f"Stripe: Processing payment of {amount}")


# Target interface 1
class PaymentABC(ABC):

    @abstractmethod
    def pay(self, order_id, amount): ...


# adpator 1
class PayPalPayment(PaymentABC):

    def pay(self, order_id, amount):
        print(order_id)
        PayPal().send_payment(amount)


# adpator 2
class StripePayment(PaymentABC):

    def pay(self, order_id, amount):
        print(order_id)
        Stripe().make_payment(amount)


"""
A single adapter handling all payment methods could lead to a violation of the Open/Closed Principle if it requires you to modify the adapter 
every time you need to support a new payment method. 
If the adapter contains a large if-else or switch-case block that has to be updated with new conditions for each new payment method, 
then it's not adhering to the principle. This design would make the adapter hard to maintain and prone to errors as it grows.
"""
