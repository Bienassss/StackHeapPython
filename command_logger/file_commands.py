from abc import ABC, abstractmethod
from file_parser import CSVDataHandler
from data_structures import Stack, Heap, MinHeap, MaxHeap


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class ExportHeapToCSVCommand(Command):
    def __init__(self, handler, numbers):
        self.handler = handler
        self.numbers = numbers
        self.backup = []

    def execute(self):
        self.backup = self.handler.read_numbers_from_csv()
        self.handler.write_numbers_to_csv_heap(self.numbers)

    def undo(self):
        self.handler.write_numbers_to_csv_heap(self.backup)

    def description(self):
        return f"ExportHeapToCSV executed with data: {self.numbers}"


class ExportStackToCSVCommand(Command):
    def __init__(self, handler, stack):
        self.handler = handler
        self.stack = stack
        self.backup = []

    def execute(self):
        self.backup = self.handler.read_numbers_from_csv()
        self.handler.write_numbers_to_csv_stack(self.stack)

    def undo(self):
        self.handler.write_numbers_to_csv_stack(self.backup)

    def description(self):
        return f"ExportStackToCSV command executed with data: {self.stack}"


class ImportFromCSVCommand(Command):
    def __init__(self, handler, target):
        self.handler = handler
        self.target = target

    def execute(self):
        try:
            numbers = self.handler.read_numbers_from_csv()
            self.target.clear()

            if isinstance(self.target, Stack):
                insert_method = self.target.push
            elif isinstance(self.target, MinHeap) or isinstance(self.target, MaxHeap):
                insert_method = self.target.insert_key
            else:
                raise ValueError("Unsupported data structure")

            for number in numbers:
                insert_method(number)

        except ValueError as e:
            print(f"Error importing numbers: {e}")

    def undo(self):
        pass

    def description(self):
        return f"ImportFromCSV executed."


class ClearCSVCommand(Command):
    def __init__(self, handler):
        self.handler = handler
        self.backup = []

    def execute(self):
        try:
            self.backup = self.handler.read_numbers_from_csv()
        except ValueError as error:
            print(f"Could not backup CSV: {error}")

        self.handler.clear_csv()

    def undo(self):
        self.handler.write_numbers_to_csv(self.backup)

    def description(self):
        return f"ClearCSVCommand executed."
