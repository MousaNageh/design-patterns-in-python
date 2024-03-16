"""
Smart Proxy Example: A smart proxy could be used to manage connections to a database. 
Instead of opening and closing connections on every query, 
the smart proxy could keep a pool of opened connections and provide them to the application when needed. 
It could also log each query for monitoring purposes or implement caching to speed up frequently made queries.
"""


class DatabaseConnection:
    def query(self, query):
        print(f"Executing query: {query}")
        # Simulate database response
        return f"Result of {query}"


class ConnectionPoolProxy:
    def __init__(self):
        self.connections = [DatabaseConnection() for _ in range(3)]
        self.query_cache = {}

    def query(self, query):
        if query in self.query_cache:
            print("Returning cached result")
            return self.query_cache[query]
        connection = self.connections.pop(0)
        result = connection.query(query)
        self.connections.append(connection)  # Return connection to the pool
        self.query_cache[query] = result
        return result


# Usage
proxy = ConnectionPoolProxy()
result1 = proxy.query("SELECT * FROM users")
print(result1)
result2 = proxy.query("SELECT * FROM users")  # This should use the cache
print(result2)


"""
anthor example 

Smart Proxy for Access Logging
In this example, we have a simple BankAccount class that allows depositing and withdrawing money.
We'll use a Smart Proxy to add logging functionality to track every time a deposit or withdrawal is made.
"""


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance


class BankAccountProxy:
    def __init__(self, real_account):
        self.real_account = real_account

    def deposit(self, amount):
        print(f"Logging: Depositing {amount}")
        return self.real_account.deposit(amount)

    def withdraw(self, amount):
        print(f"Logging: Withdrawing {amount}")
        return self.real_account.withdraw(amount)


# Usage
account = BankAccount()
proxy_account = BankAccountProxy(account)

print(proxy_account.deposit(100))  # Logging: Depositing 100
print(proxy_account.withdraw(50))  # Logging: Withdrawing 50
