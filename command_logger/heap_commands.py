from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import networkx as nx
from data_structures import MaxHeap, MinHeap, Heap


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def description(self):
        pass


class InsertKeyCommand(Command):
    def __init__(self, heap, key):
        self.heap = heap
        self.key = key
        self.executed = False

    def execute(self):
        if not self.executed:
            self.heap.insert_key(self.key)
            self.executed = True

    def undo(self):
        if self.executed:
            self.heap.delete_key(self.key)

    def description(self):
        return f"InsertKeyCommand executed in {self.heap} with data: {self.key}"


class RemoveMaxCommand(Command):
    def __init__(self, max_heap):
        self.heap = max_heap
        self.removed_item = None

    def execute(self):
        if self.heap.current_size() > 0:
            self.removed_item = self.heap.remove_max()

    def undo(self):
        if self.removed_item is not None:
            self.heap.insert_key(self.removed_item)

    def description(self):
        return f"RemoveMaxCommand executed in {self.heap}"


class RemoveMinCommand(Command):
    def __init__(self, min_heap):
        self.heap = min_heap
        self.removed_item = None

    def execute(self):
        if self.heap.current_size() > 0:
            self.removed_item = self.heap.remove_min()

    def undo(self):
        if self.removed_item is not None:
            self.heap.insert_key(self.removed_item)

    def description(self):
        return f"RemoveMinCommand executed in {self.heap}"


class PrintHeapArrayCommand(Command):
    def __init__(self, heap):
        self.heap = heap

    def execute(self):
        self.heap.print_array()

    def undo(self):
        print("Undo not supported for printing.")

    def description(self):
        return "PrintHeapArrayCommand executed."


class DrawBinaryTreeCommand(Command):
    def __init__(self, heap):
        self.heap = heap

    def execute(self):
        self.heap.draw_binary_tree()

    def undo(self):
        print("Undo not supported for drawing.")

    def description(self):
        return "DrawBinaryTreeCommand executed."
