"""
Remote Proxy Example: In a distributed system, a client application might want to interact with a service running on a remote server.
A remote proxy can act on behalf of this remote service, taking care of network communications, 
allowing the client to use the remote service as if it was a local object.
"""


# Simulated Remote Object
class RemoteService:
    def process(self):
        return "Processed data"


# Remote Proxy
class RemoteProxy:
    def __init__(self):
        self.service = RemoteService()

    def process(self):
        print("Proxying the request to the remote service")
        return self.service.process()


# Usage
proxy = RemoteProxy()
result = proxy.process()
print(result)
