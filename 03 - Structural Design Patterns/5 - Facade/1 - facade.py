"""
The Facade Design Pattern is a structural design pattern that provides a simplified interface to a complex system of classes, library, or framework.
It's like having a front-facing interface that hides the complex underlying or structural code.
The facade pattern is commonly used when a system is very complex or difficult to understand because the system has a large number of
interdependent classes or its source code is unavailable. This pattern helps to define a higher-level interface that makes the subsystem easier to use.
"""

"""
Benefits of Facade Pattern:
1 - Simplifies the Interface: By providing a simpler interface, it makes the complex system easier to use for clients.
2 - Reduces Dependencies: Clients are isolated from the components of the system, reducing the dependencies between them.
3 - Encapsulates Subsystems: Encapsulates a complex subsystem within a single interface object. This reduces the learning curve necessary to successfully leverage the subsystem.
4 - Flexibility: Allows clients to indirectly interact with the subsystem through a unified interface, making it easier to adapt or replace subsystems without affecting the client.
"""

"""
example :
a home automation system. 
Imagine you have a system that controls various aspects of your home - lights, air conditioning, and television. Individually,
these components are complex and have multiple settings and operations.
However, with a facade, you can simplify these operations with simple commands like "leaving home" or "movie night.
"""


class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class AirConditioner:
    def turn_on(self):
        print("AirConditioner is on")

    def turn_off(self):
        print("AirConditioner is off")

    def set_temperature(self, temperature):
        print(f"Setting temperature to {temperature} degrees")


class Television:
    def turn_on(self):
        print("Television is on")

    def turn_off(self):
        print("Television is off")

    def set_channel(self, channel):
        print(f"Setting channel to {channel}")


class HomeAutomationFacade:
    def __init__(self):
        self.light = Light()
        self.ac = AirConditioner()
        self.tv = Television()

    def leaving_home(self):
        self.light.turn_off()
        self.ac.turn_off()
        self.tv.turn_off()
        print("You can leave now, everything is off.")

    def movie_night(self):
        self.light.turn_off()
        self.ac.set_temperature(22)
        self.tv.turn_on()
        self.tv.set_channel("Netflix")
        print("Enjoy your movie!")


if __name__ == "__main__":
    home = HomeAutomationFacade()

    # Scenario 1: Leaving Home
    home.leaving_home()

    # Scenario 2: Movie Night
    home.movie_night()
