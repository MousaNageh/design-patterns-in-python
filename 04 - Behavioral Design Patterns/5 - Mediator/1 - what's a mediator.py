'''
The Mediator Design Pattern is a behavioral design pattern that allows us to define an object (the mediator) that encapsulates
how a set of objects(classes) interact with each other (communication). 
This pattern promotes loose coupling by keeping objects from referring to each other explicitly, 
and it allows their interaction to be varied independently. Essentially, 
the mediator acts as a hub through which all communication happens. 
In comparison to direct communication, 
where objects are aware of each other's implementation details, this method allows for better maintainability of the code.
'''
'''
Scenario: Chat Room
Consider a chat room where participants can send messages to each other. 
Without a mediator, each participant would need to know about all the other participants to send messages directly.
This setup is complex and hard to manage, especially if we want to add new features like message filtering or broadcasting messages to a subgroup of participants.
'''
from abc import ABC, abstractmethod
from typing import List


class User:
    
    def __init__(self, name: str) -> None:
        self.name = name 
        self.room:ChatRoomMediator = None
    
    def send_message(self, message):
        if self.room:
            self.room.display_message(self, message)

    def receive_message(self, message):
        print(message)
    

class ChatRoomMediator(ABC):
    @abstractmethod
    def display_message(self, user: User, message: str):
        pass


class ChatRoom(ChatRoomMediator):
    
    def __init__(self) -> None:
        self.users: List[User] = []
    
    def join(self, user: User):
        self.users.append(user)
        user.room = self    
    
    def leave(self, user: User):
        self.users.remove(user)
        user.room = None 
    
    def display_message(self, user: User, message: str):
        for u in self.users:
            if not u == user:
                u.receive_message(f"[{user.name} says]: {message}") 
                

chatroom = ChatRoom()

john = User("John")
jane = User("Jane")

chatroom.join(john)
chatroom.join(jane)

john.send_message("Hi there!")
jane.send_message("Hey John, how are you?")
                


