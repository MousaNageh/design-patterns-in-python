'''
The State design pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. 
This pattern is used when the behavior of an object should change according to its state. 
Essentially, the object will appear to change its class. 
This pattern is particularly useful for implementing finite state machines in object-oriented programming.
'''

'''
Scenario: Traffic Light System
Imagine a simple traffic light system at a road intersection. The traffic light cycles through three states: Green, Yellow, and Red. 
Each state has a distinct behavior:

Green: Indicates that vehicles can move through the intersection.
Yellow: Warns that the light is about to change to red, signaling vehicles to prepare to stop.
Red: Indicates that vehicles must stop at the intersection.
'''

from abc import ABC, abstractmethod


class TrafficLight:
    """Context class."""
    def __init__(self):
        self.state: TrafficLightState  = GreenLight()

    def change_state(self):
        self.state.change_state(self)

    def display_state(self):
        self.state.display()



class TrafficLightState(ABC):
    
    @abstractmethod
    def change_state(self, state: TrafficLight): ...
    
    @abstractmethod 
    def display(self): ...


class GreenLight(TrafficLightState):
    def change_state(self, traffic_light: TrafficLight):
        traffic_light.state = YellowLight()
        
    def display(self):
        print("Green Light - Go")

class YellowLight(TrafficLightState):
    def change_state(self, traffic_light: TrafficLight):
        traffic_light.state = RedLight()
        
    def display(self):
        print("Yellow Light - Prepare to Stop")

class RedLight(TrafficLightState):
    def change_state(self, traffic_light: TrafficLight):
        traffic_light.state = GreenLight()
        
    def display(self):
        print("Red Light - Stop")
        


# Example Usage
traffic_light = TrafficLight()
traffic_light.display_state()  # Initially, the light is green
traffic_light.change_state()   # Change to yellow
traffic_light.display_state()  # Now, the light is yellow
traffic_light.change_state()   # Change to red
traffic_light.display_state()  # Finally, the light is red