'''
single responsibility principle (SRP) else called "separation of concerns (SOC)"
god object: means putting every login in one class, it's else called 'anti pattern'
'''

# example 1 without SRP


class Journal:

    def __init__(self):
        self.counter = 0
        self.entries = []

    def add(self, text: str) -> None:
        self.counter += 1
        self.entries.append(f'{self.counter} : {text}')

    def remove_entry(self, pos: int) -> None:
        del self.entries[pos]

    def save_to_disk(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

    def load_from_disk(self, filename):
        with open(filename, 'r') as file:
            for line in file.readlines():
                self.entries.append(line.split(" : ")[1])

    def load_from_url(self, url):
        raise NotImplementedError("load_from_url not Implemented yet !")

    def __str__(self):
        return '\n'.join(self.entries)

# we break the SRP because we add extra functionality to the class , not just add or remove text
# but else load and save file to disk
# if me have another class that will load data from disk or save data to disk

# let us solve this


class Journal2:

    def __init__(self):
        self.counter = 0
        self.entries = []

    def add(self, text: str) -> None:
        self.counter += 1
        self.entries.append(f'{self.counter} : {text}')

    def remove_entry(self, pos: int) -> None:
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:

    @staticmethod
    def load_from_disk(filename: str, class_instance, list_name: str):
        with open(filename, 'r') as file:
            for line in file.readlines():
                list_to_read = getattr(class_instance, list_name)
                list_to_read.append(line.split(" : ")[1])

    @staticmethod
    def save_to_disk(filename, class_instance):
        with open(filename, 'w') as file:
            file.write(str(class_instance))


# usage of our code
j = Journal2()
j.add("first statement")
j.add("second statement")
PersistenceManager.save_to_disk("file.txt", j)

j2 = Journal2()
PersistenceManager.load_from_disk("file.txt", j2, 'entries')
print(j2)
