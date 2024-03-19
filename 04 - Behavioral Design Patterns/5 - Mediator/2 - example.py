'''
Scenario: Air Traffic Control
Imagine an airport with multiple runways and several flights wanting to take off or land at any given time.
Without a mediator, each flight would need to communicate with all other flights to manage takeoffs, landings, 
and avoid collisions. This system would be highly complex and error-prone, as the number of flights increases.

Objective: Implement a Mediator pattern where an AirTrafficControl acts as the mediator between Flights.
The Flights will request permission to take off or land,
and the AirTrafficControl will manage these requests to ensure that only one flight uses a runway at a time.

Here are the components you'll need to design:

AirTrafficControlMediator Interface: An interface that defines the method for receiving requests from flights.

AirTrafficControl: A concrete mediator class that implements the AirTrafficControlMediator interface. 
It will handle the logic to manage runway availability and coordinate the flights' actions.

Flight: Represents an airplane that wants to take off or land. Each Flight knows the AirTrafficControl it must communicate with 
but doesn't communicate directly with other flights.

'''
from abc import ABC, abstractmethod
from typing import List

class Flight:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.air_traffic_controller: 'AirTrafficControlMediator' = None
    
    def land(self):
        self.air_traffic_controller.land(self)
    
    def take_off(self):
        self.air_traffic_controller.take_off(self)
    
    def notification(self, message: str):
        print(f"{self.name} received notification: {message}")

    def land_approved(self):
        print(f"{self.name} land request approved")
    
    def take_off_approved(self):
        print(f"{self.name} take off request approved")

class AirTrafficControlMediator(ABC):
    
    @abstractmethod
    def land(self, flight: Flight) -> None: ...
    
    @abstractmethod
    def take_off(self, flight: Flight) -> None: ...

class AirTrafficControl(AirTrafficControlMediator):
    
    def __init__(self) -> None:
        self.flights: List[Flight] = []
    
    def land(self, flight: Flight):
        for f in self.flights:
            if f != flight:
                f.notification(f"{flight.name} has a request to land.")
        flight.land_approved()
    
    def take_off(self, flight: Flight):
        for f in self.flights:
            if f != flight:
                f.notification(f"{flight.name} has a request to take off.")
        flight.take_off_approved()
    
    def add_flight(self, *flights: Flight) -> None:
        for flight in flights:
            flight.air_traffic_controller = self
        self.flights.extend(flights)

f1 = Flight(name='f1')
f2 = Flight(name='f2')
f3 = Flight(name='f3')
control = AirTrafficControl()
control.add_flight(f1, f2, f3)

f1.land()
