class Stack():
    def __init__(self):
        self._stack_contents = []

    def push(self, item):
        self._stack_contents.append(item)

    def peek(self):
        if not self.is_empty():
            return self._stack_contents[-1]
        else:
            print("Stack is empty.")
            return None

    def pop(self):
        if not self.is_empty():
            return self._stack_contents.pop()
        else:
            print("Stack is empty.")
            return None 

    def is_empty(self):
        return len(self._stack_contents) == 0  

    def print_array(self):
        for stack_index in range(len(self._stack_contents)):
            print(self._stack_contents[stack_index], end=' ')
        print()

    def return_stack_contents(self):
        return self._stack_contents.copy()

    def clear(self):
        self._stack_contents = []
