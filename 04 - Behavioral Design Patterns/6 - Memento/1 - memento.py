'''
The Memento design pattern is a behavioral design pattern that allows an object to save its state so that it can be restored to this state later,
without breaking the encapsulation of its implementation details. 
This pattern is particularly useful for features like undo mechanisms in applications.

Core Components of the Memento Pattern:
1 - Originator: The object whose state needs to be saved and restored.
2 - Memento: The object that stores the state of the originator. 
3 - Caretaker: The object that keeps track of the mementos. The caretaker decides when to save or restore the originator's state but doesn't modify the mementos itsel
'''
'''
Let's create a Python example that demonstrates the Memento Design Pattern through a simple text editor scenario. 
This example will include the functionality to undo and redo text changes.
'''

class EditorMemento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content

class Editor:
    def __init__(self):
        self._content = ""
        self._states = []
        self._current_state = -1

    def type(self, words):
        self._content += words
        self._save_state()

    def _save_state(self):
        memento = EditorMemento(self._content)
        self._states = self._states[:self._current_state + 1]  # Remove redo history after new edit
        self._states.append(memento)
        self._current_state += 1

    def undo(self):
        if self._current_state > 0:
            self._current_state -= 1
            self._content = self._states[self._current_state].get_content()
        else:
            print("No more undos available.")

    def redo(self):
        if self._current_state < len(self._states) - 1:
            self._current_state += 1
            self._content = self._states[self._current_state].get_content()
        else:
            print("No more redos available.")

    def print_content(self):
        print(self._content)

# Example usage
editor = Editor()

editor.type("First sentence. ")
editor.type("Second sentence. ")

editor.print_content()  # Output: First sentence. Second sentence.

editor.undo()
editor.print_content()  # Output: First sentence.

editor.undo()
editor.print_content()  # Output: (empty)

editor.redo()
editor.print_content()  # Output: First sentence.

editor.redo()
editor.print_content()  # Output: First sentence. Second sentence.