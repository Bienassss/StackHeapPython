import unittest
import sys
sys.path.append('/home/benas/Python/Python Project/StackHeapPython')  
from data_structures.heap import MaxHeap

class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        # Initialize a MaxHeap with a capacity of 10 elements before each test
        self.heap = MaxHeap(10)

    def test_initialization(self):
        # Check if the heap is empty upon initialization
        self.assertEqual(self.heap.current_size(), 0)

    def test_insert_key(self):
        # Insert multiple keys and check if the maximum is correct
        keys = [10, 3, 5, 2, 15]
        for key in keys:
            self.heap.insert_key(key)
        self.assertEqual(self.heap.get_max(), 15)

    def test_remove_max(self):
        # Remove the maximum element and check if the heap property is maintained
        keys = [5, 3, 8, 20, 2]
        for key in keys:
            self.heap.insert_key(key)
        max_val = self.heap.remove_max()
        self.assertEqual(max_val, 20)
        self.assertNotEqual(self.heap.get_max(), 20)

    def test_get_max(self):
        # Ensure get_max returns the maximum element without removing it
        self.heap.insert_key(2)
        self.heap.insert_key(100)
        self.assertEqual(self.heap.get_max(), 100)

    def test_increase_key(self):
        # Increase a key's value and ensure the heap property is maintained
        keys = [4, 10, 3]
        for key in keys:
            self.heap.insert_key(key)
        self.heap.increase_key(2, 50)  # Index 2 is assumed to have been key '3'
        self.assertEqual(self.heap.get_max(), 50)

    def test_clear(self):
        # Clear the heap and ensure it's empty
        keys = [4, 2, 5, 100]
        for key in keys:
            self.heap.insert_key(key)
        self.heap.clear()
        self.assertEqual(self.heap.current_size(), 0)

if __name__ == "__main__":
    unittest.main()


