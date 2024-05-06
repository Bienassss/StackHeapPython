import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore


class Heap:
    def __init__(self, max_heap_size):
        self._max_heap_size = max_heap_size
        self._arr = [None] * max_heap_size
        self._heap_size = 0

    def _parent(self, heap_index):
        return (heap_index - 1) // 2

    def _left_child(self, heap_index):
        return 2 * heap_index + 1

    def _right_child(self, heap_index):
        return 2 * heap_index + 2

    def current_size(self):
        return self._heap_size

    def insert_key(self, key):
        if self._heap_size == self._max_heap_size:
            print("Overflow: Could not insert key")
            return
        self._heap_size += 1
        heap_index = self._heap_size - 1
        self._arr[heap_index] = key
        self._bubble_up(heap_index)
        self._heapify(heap_index)

    def _heapify(self, heap_index):
        raise NotImplementedError(
            "This method should be overridden by subclasses.")

    def _bubble_up(self, heap_index):
        raise NotImplementedError(
            "This method should be overridden by subclasses.")

    def draw_binary_tree(self):
        G = nx.DiGraph()

        for heap_index in range(self._heap_size):
            G.add_node(heap_index, label=str(self._arr[heap_index]))

            parent_index = self._parent(heap_index)
            if heap_index != 0 and parent_index < self._heap_size:
                G.add_edge(parent_index, heap_index)

        pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot')
        nx.draw(G, pos, with_labels=False, arrows=False)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw_networkx_labels(G, pos, labels=labels)

        plt.show()

    def print_array(self):
        for heap_index in range(self._heap_size):
            print(self._arr[heap_index], end=' ')
        print()

    def return_heap_contents(self):
        numbers = self._arr[:self._heap_size]
        return numbers

    def clear(self):
        self._arr = [None] * self._max_heap_size
        self._heap_size = 0


class MaxHeap(Heap):
    def __init__(self, max_heap_size):
        super().__init__(max_heap_size)

    def _bubble_up(self, heap_index):
        while heap_index != 0 and self._arr[self._parent(
                heap_index)] < self._arr[heap_index]:
            self._arr[heap_index], self._arr[self._parent(
                heap_index)] = self._arr[self._parent(heap_index)], self._arr[heap_index]
            heap_index = self._parent(heap_index)

    def _heapify(self, heap_index):
        largest = heap_index
        left = self._left_child(heap_index)
        right = self._right_child(heap_index)

        if left < self._heap_size and self._arr[left] > self._arr[largest]:
            largest = left
        if right < self._heap_size and self._arr[right] > self._arr[largest]:
            largest = right
        if largest != heap_index:
            self._arr[heap_index], self._arr[largest] = self._arr[largest], self._arr[heap_index]
            self._heapify(largest)

    def remove_max(self):
        if self._heap_size <= 0:
            return None
        if self._heap_size == 1:
            self._heap_size -= 1
            return self._arr[0]

        root = self._arr[0]
        self._arr[0] = self._arr[self._heap_size - 1]
        self._heap_size -= 1
        self._heapify(0)
        return root

    def increase_key(self, heap_index, newVal):
        self._arr[heap_index] = newVal
        self._bubble_up(heap_index)

    def get_max(self):
        if self._heap_size > 0:
            return self._arr[0]
        return None

    def delete_key(self, heap_index):

        if self._heap_size == 0:
            print("Error: Heap is empty.")
            return
        if not 0 <= heap_index < self._heap_size:
            print("Error: Index out of range.")
            return

        self.increase_key(heap_index, float("inf"))

        self.remove_max()

        for i in range((self._heap_size // 2) - 1, -1, -1):
            self._heapify(i)

    def insert_key(self, key):
        super().insert_key(key)

    def draw_binary_tree(self):
        super().draw_binary_tree()

    def print_array(self):
        print("MaxHeap array contents:")
        super().print_array()

    def return_heap_contents(self):
        numbers = self._arr[:self._heap_size]
        return numbers

    def clear(self):
        super().clear()


class MinHeap(Heap):
    def __init__(self, max_heap_size):
        super().__init__(max_heap_size)

    def _bubble_up(self, heap_index):
        while heap_index != 0 and self._arr[self._parent(
                heap_index)] > self._arr[heap_index]:
            self._arr[heap_index], self._arr[self._parent(
                heap_index)] = self._arr[self._parent(heap_index)], self._arr[heap_index]
            heap_index = self._parent(heap_index)

    def _heapify(self, heap_index):
        smallest = heap_index
        left = self._left_child(heap_index)
        right = self._right_child(heap_index)

        if left < self._heap_size and self._arr[left] < self._arr[smallest]:
            smallest = left
        if right < self._heap_size and self._arr[right] < self._arr[smallest]:
            smallest = right
        if smallest != heap_index:
            self._arr[heap_index], self._arr[smallest] = self._arr[smallest], self._arr[heap_index]
            self._heapify(smallest)

    def remove_min(self):
        if self._heap_size <= 0:
            return None
        if self._heap_size == 1:
            self._heap_size -= 1
            return self._arr[0]

        root = self._arr[0]
        self._arr[0] = self._arr[self._heap_size - 1]
        self._heap_size -= 1
        self._heapify(0)
        return root

    def decrease_key(self, heap_index, newVal):
        self._arr[heap_index] = newVal
        self._bubble_up(heap_index)

    def get_min(self):
        if self._heap_size > 0:
            return self._arr[0]
        return None

    def delete_key(self, heap_index):
        self.decrease_key(heap_index, float("-inf"))
        self.remove_min()

    def insert_key(self, key):
        super().insert_key(key)

    def draw_binary_tree(self):
        super().draw_binary_tree()

    def print_array(self):
        print("MinHeap array contents:")
        super().print_array()

    def return_heap_contents(self):
        numbers = self._arr[:self._heap_size]
        return numbers

    def clear(self):
        super().clear()
