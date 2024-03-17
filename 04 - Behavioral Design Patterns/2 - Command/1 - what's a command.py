"""

The Command design pattern is a behavioral design pattern that turns a request into a stand-alone object containing all information about the request.
This transformation allows you to parameterize methods with different requests, 
delay or queue a request's execution, and support undoable operations.
"""

"""
Scenario:
Imagine you're developing a text editor, and you want to implement functionality to perform various text operations like Copy, Paste, and Undo. 
These operations should be performed on command, and you should be able to undo them. 
Using the Command pattern, you can encapsulate each operation in its own object, 
allowing you to store a history of operations for undo functionality and to execute operations without directly knowing the operation's details.
"""

from abc import ABC, abstractmethod


# Receiver
class TextEditor:
    def __init__(self, text=""):
        self.text = text
        self.clipboard = ""

    def copy(self):
        self.clipboard = self.text

    def paste(self):
        self.text += self.clipboard


# The Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Commands
class CopyCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.previous_text = ""

    def execute(self):
        self.previous_text = self.editor.text
        self.editor.copy()

    def undo(self):
        self.editor.text = self.previous_text


class PasteCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.previous_text = ""

    def execute(self):
        self.previous_text = self.editor.text
        self.editor.paste()

    def undo(self):
        self.editor.text = self.previous_text


# Invoker
class CommandManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()


# Client code
if __name__ == "__main__":
    editor = TextEditor()
    editor.text = "Hello"

    copy_command = CopyCommand(editor)
    paste_command = PasteCommand(editor)
    command_manager = CommandManager()

    command_manager.execute_command(copy_command)
    print(editor.text)  # Output: Hello

    command_manager.execute_command(paste_command)
    print(editor.text)  # Output: HelloHello

    command_manager.undo()
    print(editor.text)  # Output: Hello (Undo paste)

    command_manager.undo()
    print(editor.text)  # Output: Hello (Nothing changes, undo copy doesn't affect text)
