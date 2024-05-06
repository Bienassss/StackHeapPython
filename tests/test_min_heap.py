import unittest
import sys
sys.path.append('/home/benas/Python/Python Project/StackHeapPython')  
from data_structures.heap import MinHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap(10)

    def test_initialization(self):
        self.assertTrue(self.heap.current_size() == 0)

    def test_insert_key(self):
        keys = [3, 1, 2]
        for key in keys:
            self.heap.insert_key(key)
        self.assertEqual(self.heap.get_min(), 1)

    def test_remove_min(self):
        keys = [5, 3, 8, 1, 2]
        for key in keys:
            self.heap.insert_key(key)
        min_val = self.heap.remove_min()
        self.assertEqual(min_val, 1)
        self.assertNotEqual(self.heap.get_min(), 1)

    def test_get_min(self):
        self.heap.insert_key(2)
        self.heap.insert_key(1)
        self.assertEqual(self.heap.get_min(), 1)

    def test_decrease_key(self):
        keys = [5, 6, 7]
        for key in keys:
            self.heap.insert_key(key)
        self.heap.decrease_key(2, 1)  # Decrease key of index 2 which was 7 to 1
        self.assertEqual(self.heap.get_min(), 1)

    def test_clear(self):
        keys = [4, 2, 5, 1]
        for key in keys:
            self.heap.insert_key(key)
        self.heap.clear()
        self.assertEqual(self.heap.current_size(), 0)

    def test_heapify(self):
        self.heap.insert_key(10)
        self.heap.insert_key(20)
        self.heap.insert_key(5)
        self.heap.insert_key(6)
        self.heap.insert_key(2)
        self.heap._heapify(0)
        self.assertEqual(self.heap.get_min(), 2)

if __name__ == '__main__':
    unittest.main()
