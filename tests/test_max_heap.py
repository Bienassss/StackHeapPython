import unittest
import sys
sys.path.append('/home/benas/Python/Python Project/StackHeapPython')  
from data_structures.heap import MaxHeap

class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap(10)

    def test_initialization(self):
        self.assertEqual(self.heap.current_size(), 0)

    def test_insert_key(self):
        keys = [10, 3, 5, 2, 15]
        for key in keys:
            self.heap.insert_key(key)
        self.assertEqual(self.heap.get_max(), 15)

    def test_remove_max(self):
        keys = [5, 3, 8, 20, 2]
        for key in keys:
            self.heap.insert_key(key)
        max_val = self.heap.remove_max()
        self.assertEqual(max_val, 20)
        self.assertNotEqual(self.heap.get_max(), 20)

    def test_get_max(self):
        self.heap.insert_key(2)
        self.heap.insert_key(100)
        self.assertEqual(self.heap.get_max(), 100)

    def test_increase_key(self):
        keys = [4, 10, 3]
        for key in keys:
            self.heap.insert_key(key)
        self.heap.increase_key(2, 50)  # Index 2 is assumed to have been key '3'
        self.assertEqual(self.heap.get_max(), 50)

    def test_clear(self):
        keys = [4, 2, 5, 100]
        for key in keys:
            self.heap.insert_key(key)
        self.heap.clear()
        self.assertEqual(self.heap.current_size(), 0)

if __name__ == "__main__":
    unittest.main()


