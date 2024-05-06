import unittest
import sys
sys.path.append('/home/benas/Python/Python Project/StackHeapPython')  
from data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_initialization(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.return_stack_contents(), [1])

    def test_peek(self):
        self.stack.push(2)
        top_item = self.stack.peek()
        self.assertEqual(top_item, 2)
        self.assertEqual(self.stack.return_stack_contents(), [2])

    def test_peek_empty(self):
        top_item = self.stack.peek()
        self.assertIsNone(top_item)

    def test_pop(self):
        self.stack.push(3)
        self.stack.push(4)
        popped_item = self.stack.pop()
        self.assertEqual(popped_item, 4)
        self.assertEqual(self.stack.return_stack_contents(), [3])

    def test_pop_empty(self):
        popped_item = self.stack.pop()
        self.assertIsNone(popped_item)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())

    def test_return_stack_contents(self):
        items = [1, 2, 3]
        for item in items:
            self.stack.push(item)
        self.assertEqual(self.stack.return_stack_contents(), items)

    def test_clear(self):
        self.stack.push(6)
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())

if __name__ == "__main__":
    unittest.main()
