'''
Imagine a system designed to control different types of devices (e.g., TVs, Radios) 
with different types of remote controls (e.g., Basic Remote, Advanced Remote with additional features like voice control). 
Without the Bridge design pattern, for each device type, you would need a separate class for each type of remote control. 
This approach would not only result in a significant number of classes as the number of devices and remote types grows but also makes it hard to add new features or device types without extensive reworking and code duplication.
'''

# Implementor (Remote Control)
class RemoteControl:
    def on_button_pressed(self):
        pass
    
    def off_button_pressed(self):
        pass


# Concrete Implementor 1
class BasicRemote(RemoteControl):
    def on_button_pressed(self):
        print("Power ON")

    def off_button_pressed(self):
        print("Power OFF")


# Concrete Implementor 2
class AdvancedRemote(BasicRemote):
    def mute_button_pressed(self):
        print("Mute")

# Abstraction (Device)
class Device:
    def __init__(self, remote):
        self.remote = remote
    
    def turn_on(self):
        self.remote.on_button_pressed()
    
    def turn_off(self):
        self.remote.off_button_pressed()

# Refined Abstraction 1
class TV(Device):
    pass

# Refined Abstraction 2
class Radio(Device):
    pass