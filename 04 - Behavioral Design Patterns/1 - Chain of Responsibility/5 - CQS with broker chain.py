class ICommand:
    def execute(self):
        pass


class IQuery:
    def execute(self):
        pass


class MovePlayerCommand(ICommand):
    def __init__(self, direction):
        self.direction = direction

    def execute(self):
        print(f"Moving player {self.direction}")


class GetPlayerHealthQuery(IQuery):
    def execute(self):
        # Assume the player's health is 100 for this example
        return 100


class Broker:
    def __init__(self):
        self._subscribers = {"command": [], "query": []}

    def subscribe(self, message_type, handler):
        self._subscribers[message_type].append(handler)

    def publish_command(self, command):
        for handler in self._subscribers["command"]:
            handler.execute(command)

    def publish_query(self, query):
        for handler in self._subscribers["query"]:
            return handler.execute(query)


# Usage
broker = Broker()
broker.subscribe("command", MovePlayerCommand("north"))
health = GetPlayerHealthQuery()
broker.subscribe("query", health)

broker.publish_command(MovePlayerCommand("north"))
print(f"Player health: {broker.publish_query(health)}")
