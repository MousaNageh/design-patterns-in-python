"""
The Broker Chain is a variation of the Chain of Responsibility design pattern,
--often used in event-driven architectures or when implementing a centralized event handling system--. 
This variation introduces a centralized broker or mediator that manages the communication between handlers, 
instead of having each handler directly call the next one in the chain. 
The handlers, in this case, 
subscribe to the broker for the events (or commands) they are interested in handling, 
and the broker dispatches incoming events to all subscribed handlers.

Key Components of the Broker Chain
1 - Broker/Mediator: Acts as the central point of communication. 
    It keeps track of subscriptions and forwards events to subscribed handlers. 
    The broker is responsible for managing the chain dynamically, 
    allowing handlers to subscribe or unsubscribe from certain events or commands at runtime.

2 - Handlers/Participants: These are the objects that handle specific types of events. 
    Handlers register with the broker to express interest in handling particular events. 
    When an event occurs, the broker notifies all registered handlers, who then have the opportunity to process the event.
"""

from abc import ABC, abstractmethod


class DocumentReaderABC(ABC):
    @abstractmethod
    def read(self, files_path: str): ...


class PDFReader(DocumentReaderABC):
    def read(self, files_path: str):
        print("reading PDF file")


class DOCXReader(DocumentReaderABC):
    def read(self, files_path: str):
        print("reading DOCX file")


class TXTReader(DocumentReaderABC):
    def read(self, files_path: str):
        print("reading TXT file")


class Reader:

    def __init__(self):
        self._subscribers = {}

    def subscribe(self, doc_type: str, handler: DocumentReaderABC):
        if doc_type not in self._subscribers:
            self._subscribers[doc_type] = []
        self._subscribers[doc_type.lower()].append(handler)

    def publish(self, file_path: str):
        handlers = self._subscribers.get(self.__get_extension(file_path), [])
        for handler in handlers:
            handler.read(file_path)

    def __get_extension(self, file_path: str):
        _, extension = file_path.rsplit(".", 1)
        return extension.lower()


reader = Reader()
text_reader = TXTReader()
docs_reader = DOCXReader()
pdf_reader = PDFReader()

reader.subscribe(doc_type="pdf", handler=pdf_reader)
reader.subscribe(doc_type="txt", handler=text_reader)
reader.subscribe(doc_type="docs", handler=docs_reader)

reader.publish("mousa.pdf")


"""
Example Scenario
Imagine a scenario where a game engine uses a Broker Chain to handle events like 
"player health changes", "item pickup", and "enemy defeated". 
Different systems within the game engine (e.g., UI system, audio system, achievement system) are interested in these events for various reasons:

The UI System needs to update the player's health bar or inventory display.
The Audio System plays specific sounds when items are picked up or enemies are defeated.
The Achievement System tracks certain milestones, like defeating a certain number of enemies.
"""


class EventBroker:
    def __init__(self):
        self._subscribers = dict()

    def subscribe(self, event_type, handler):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    def publish(self, event_type, data=None):
        if event_type in self._subscribers:
            for handler in self._subscribers[event_type]:
                handler(data) if data else handler()


class UISystem:
    def on_player_health_changes(self, health):
        print(f"UI System: Player health changed to {health}.")


class AudioSystem:
    def on_item_pickup(self, item):
        print(f"Audio System: Playing pickup sound for {item}.")


class AchievementSystem:
    def on_enemy_defeated(self):
        print("Achievement System: Enemy defeated achievement progress updated.")


if __name__ == "__main__":
    # Create the event broker
    broker = EventBroker()

    # Create systems
    ui_system = UISystem()
    audio_system = AudioSystem()
    achievement_system = AchievementSystem()

    # Subscribe systems to events
    broker.subscribe("player_health_changes", ui_system.on_player_health_changes)
    broker.subscribe("item_pickup", audio_system.on_item_pickup)
    broker.subscribe("enemy_defeated", achievement_system.on_enemy_defeated)

    # Simulate some game events
    broker.publish("player_health_changes", 90)
    broker.publish("item_pickup", "Sword of Destiny")
    broker.publish("enemy_defeated")

#######################################
