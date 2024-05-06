from abc import ABC, abstractmethod
from data_structures import Stack


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class PushCommand(Command):
    def __init__(self, stack, item):
        self.stack = stack
        self.item = item

    def execute(self):
        self.stack.push(self.item)

    def undo(self):
        if not self.stack.is_empty():
            self.stack.pop()

    def description(self):
        return f"PushCommand executed in {self.stack} with data: {self.item}"


class PopCommand(Command):
    def __init__(self, stack):
        self.stack = stack
        self.item = None

    def execute(self):
        if not self.stack.is_empty():
            self.item = self.stack.pop()

    def undo(self):
        if self.item is not None:
            self.stack.push(self.item)

    def description(self):
        return f"PushCommand executed in {self.stack}"


class PrintStackArrayCommand(Command):
    def __init__(self, stack):
        self.stack = stack

    def execute(self):
        self.stack.print_array()

    def undo(self):
        print("Undo not supported for printing.")

    def description(self):
        return "PrintStackArrayCommand executed."
