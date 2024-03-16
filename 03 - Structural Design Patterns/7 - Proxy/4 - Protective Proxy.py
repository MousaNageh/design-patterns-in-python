'''
Protective Proxy Example: Consider a document editor where documents can be accessed and modified by different users. 
A protective proxy could control access to documents based on the user's permissions, allowing only authorized users to make changes.
'''

class Document:
    def __init__(self, content):
        self.content = content

class ProtectiveProxy:
    def __init__(self, document, user):
        self.document = document
        self.user = user

    def read(self):
        return self.document.content

    def write(self, content):
        if self.user == "authorized_user":
            self.document.content = content
        else:
            raise Exception("User is not authorized to write.")

# Usage
doc = Document("Secret Content")
proxy = ProtectiveProxy(doc, "unauthorized_user")
print(proxy.read())  # Allowed for any user
try:
    proxy.write("New Content")  # Raises exception
except Exception as e:
    print(e)

proxy = ProtectiveProxy(doc, "authorized_user")
proxy.write("New Content")  # Success for authorized user
print(proxy.read())


'''
example 2 
'''
class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young')


car = CarProxy(Driver('John', 12))
car.drive()