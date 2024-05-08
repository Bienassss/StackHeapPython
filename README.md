# Coursework Report
## Introduction

### Goal of the Coursework
The primary goal of this coursework is to develop a program that operates as a testing tool for observing and understanding the behavior of heap and stack data structures through practical operations, while incorporating object-oriented programming (OOP) principles. This application is designed to enable students and software developers to visually and interactively explore how these data structures function and handle data in various scenarios, thereby enhancing their grasp of various forms of data management in software development.

### About the Application
Our application, named Shade [ Stack-Heap And Data Engineering ], is a Python console application that focuses on demonstrating and testing operations within heap and stack data structures. It is designed to allow users to perform various operations such as inserting elements, printing the stack, and visualizing heaps as binary trees. Additionally, the application supports importing and exporting data from .csv files according to the type of data structure being manipulated. This functionality is particularly useful for educational purposes, enabling users to explore and understand the dynamic behavior of these fundamental data structures in computing.

### How to Run the Program
To run the program, follow these steps:
1. Ensure that Python is installed on your computer.
2. Download the source code from [Github](https://github.com/Bienassss/StackHeapPython).
3. Open your Python IDE and compile the code.


### How to Use the Program

Using the program is straightforward:

#### Start the Application
- **Run the Code:** Open your IDE (Integrated Development Environment) and execute the code. This will launch the program.

#### Navigating the Interface
- **Access the Interface:** Once the code is running, an interface will appear in the command terminal.
- **Menu Selection:** Use the menu to navigate through the application. Type the number corresponding to your desired action and press 'Enter' to select it.

#### Performing Tasks
- **Operations on Data Structures:** To perform operations on heaps and stacks, navigate to their respective menu pages.
- **Importing Data:**
  - If you need to handle larger sets of numerical data, consider importing it from a `.csv` file.
  - **Creating a CSV File:** You can create a `.csv` file named `my_numbers.csv` in the application's directory either by using the export feature of the program or by manually entering numbers into a new file.
  - **Using Existing Data:** To import data, ensure the `.csv` file is placed in the application’s directory and select the import option from the menu.


## Body/Analysis

### Implementation of Functional Requirements
This section of the report discusses how the application meets its functional requirements through its features and design. Below are some of the key functionalities implemented:


### Stack Data Structure:

#### Feature 1: Push
- **Description:** Adds an element to the top of the stack.
- **Code Snippet:**
    ```python
    def push(self, item):
        self._stack_contents.append(item)
    ```

#### Feature 2: Pop
- **Description:** Removes the element at the top of the stack and returns it. If the stack is empty, it returns `None` and prints a message.
- **Code Snippet:**
    ```python
    def pop(self):
        if not self.is_empty():
            return self._stack_contents.pop()
        else:
            print("Stack is empty.")
            return None
    ```

#### Feature 3: Peek
- **Description:** Returns the element at the top of the stack without removing it. If the stack is empty, it returns `None` and prints a message.
- **Code Snippet:**
    ```python
    def peek(self):
        if not self.is_empty():
            return self._stack_contents[-1]
        else:
            print("Stack is empty.")
            return None
    ```

#### Feature 4: Is Empty
- **Description:** Checks if the stack is empty. Returns `True` if empty, `False` otherwise.
- **Code Snippet:**
    ```python
    def is_empty(self):
        return len(self._stack_contents) == 0
    ```

#### Feature 5: Print Array
- **Description:** Prints all elements in the stack from bottom to top.
- **Code Snippet:**
    ```python
    def print_array(self):
        for stack_index in range(len(self._stack_contents)):
            print(self._stack_contents[stack_index], end=' ')
        print()
    ```

#### Feature 6: Return Stack Contents
- **Description:** Returns a copy of the stack's contents without modifying the original stack.
- **Code Snippet:**
    ```python
    def return_stack_contents(self):
        return self._stack_contents.copy()
    ```

#### Feature 7: Clear
- **Description:** Clears all elements from the stack, effectively resetting it.
- **Code Snippet:**
    ```python
    def clear(self):
        self._stack_contents = []
    ```



### Heap Data Structure:

#### Feature 1: Insert Key
- **Description:** Adds an element to the heap. The element is initially added to the end of the array, and then the heap properties are restored by bubbling the element up as necessary. This method is inherited by both subclasses.
- **Code Snippet:**
    ```python
    def insert_key(self, key):
        if self._heap_size == self._max_heap_size:
            print("Overflow: Could not insert key")
            return
        self._heap_size += 1
        heap_index = self._heap_size - 1
        self._arr[heap_index] = key
        self._bubble_up(heap_index)
        self._heapify(heap_index)
    ```

#### Feature 2: Bubble Up
- **Description:** The `bubble up` (or "percolate up") method is essential for maintaining the heap property after a new key is inserted at the bottom of the heap. This method iteratively compares the inserted element with its parent, swapping them if the heap condition (maximum or minimum) is not satisfied. This process continues until the element is in a position where the heap property is correctly maintained. This method as many others in these two subclasses follows the principle of Polymorphism by having different implementations in either class while retaining the same method signature.

- **Base Implementation:**
    ```python
    def _bubble_up(self, heap_index):
        raise NotImplementedError(
            "This method should be overridden by subclasses to define bubble up logic.")
    ```

- **Implementation in MaxHeap:**
    - **Description:** In a MaxHeap, `bubble up` ensures that any newly inserted element rises to its correct position so that every parent node is larger than or equal to its children. This maintains the max-heap property, where the highest element is always at the root.
    - **Code Snippet:**
    ```python
    def _bubble_up(self, heap_index):
        while heap_index != 0 and self._arr[self._parent(
                heap_index)] < self._arr[heap_index]:
            self._arr[heap_index], self._arr[self._parent(
                heap_index)] = self._arr[self._parent(heap_index)], self._arr[heap_index]
            heap_index = self._parent(heap_index)
    ```


- **Implementation in MinHeap:**
    - **Description:** Conversely, in a MinHeap, the `bubble up` process ensures that the newly inserted element moves up the heap structure until it is no longer smaller than its parent. This operation is crucial for maintaining the min-heap property, which requires the smallest element to be at the root.
    - **Code Snippet:**
    ```python
    def _bubble_up(self, heap_index):
        while heap_index != 0 and self._arr[self._parent(
                heap_index)] > self._arr[heap_index]:
            self._arr[heap_index], self._arr[self._parent(
                heap_index)] = self._arr[self._parent(heap_index)], self._arr[heap_index]
            heap_index = self._parent(heap_index)
    ```


These detailed explanations and implementations highlight how the `bubble up` method functions differently in MaxHeap and MinHeap settings, underlining the polymorphic nature of this method and its importance in maintaining the integrity of heap structures.


#### Feature 3: Heapify
- **Description:** The `heapify` method is critical for maintaining the heap property across the entire data structure after any modifications, such as insertions or deletions. It ensures that the heap continues to meet its condition as a max-heap or min-heap by adjusting the positions of elements within the heap. This method is designed to be overridden in subclasses, following the principle of polymorphism, which allows each subclass to implement its specific behavior while adhering to a general contract.

- **Base Implementation:**
    ```python
    def _heapify(self, heap_index):
        raise NotImplementedError(
            "This method should be overridden by subclasses to provide specific heapify behavior.")
    ```

- **Implementation in MaxHeap:**
    - **Description:** In the MaxHeap, `heapify` adjusts the heap to maintain the maximum heap condition after changes. It compares the parent node with its children and swaps them to ensure the parent is the largest of the three, continuing the process recursively as needed.
    - **Code Snippet:**
    ```python
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

    ```


- **Implementation in MinHeap:**
    - **Description:** For the MinHeap, the `heapify` method works similarly but maintains the minimum heap condition. It ensures that the parent node is the smallest among its children. This method is crucial for the heap to continue functioning as a priority queue where the smallest element is always accessible at the root.
    - **Code Snippet:**
    ```python
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
    ```


#### Feature 4: Draw Binary Tree
- **Description:** Visualizes the heap as a binary tree. This function helps in understanding the structure of the heap after several operations.
- **Code Snippet:**
    ```python
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
    ```

#### Feature 5: Print Array
- **Description:** Outputs the current contents of the heap array. This is useful for debugging and verification of the heap's current state.
- **Code Snippet:**
    ```python
    def print_array(self):
        for heap_index in range(self._heap_size):
            print(self._arr[heap_index], end=' ')
        print()
    ```

#### Feature 6: Clear Heap
- **Description:** Resets the heap by clearing all elements from the heap array. This is useful for reinitializing the heap during testing or after completing certain operations.
- **Code Snippet:**
    ```python
    def clear(self):
        self._arr = [None] * self._max_heap_size
        self._heap_size = 0
    ```

#### Feature 7: Return Heap Contents
- **Description:** Returns a list of all active elements in the heap. This allows other parts of the program or external systems to access heap data without directly interacting with the heap structure. 
- **Code Snippet:**
    ```python
    def return_heap_contents(self):
        return self._arr[:self._heap_size]
    ```
    
#### Feature 8: Remove Max/Min
- **Description (MaxHeap - Remove Max):** Removes and returns the maximum element from the heap. This operation also ensures the heap property is maintained after the removal. If the heap is empty, it returns `None`.
- **Code Snippet (MaxHeap - Remove Max):**
    ```python
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
    ```

- **Description (MinHeap - Remove Min):** Removes and returns the minimum element from the heap. Similar to the max operation, this maintains the heap's structure and property after the element is removed. Returns `None` if the heap is empty.
- **Code Snippet (MinHeap - Remove Min):**
    ```python
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
    ```

These features encapsulate critical operations in heap management, ensuring that both MaxHeap and MinHeap can efficiently serve their purpose in a variety of applications where either maximum or minimum elements are periodically needed for further processing.
#### Feature 9: Get Max/Min 
#### Get Max (MaxHeap)
- **Description:** Retrieves the maximum element from the heap without removing it. This method is fundamental in max-heap operations where quick access to the largest element is frequently required. It simply returns the element at the root of the heap, ensuring constant time complexity, O(1). If the heap is empty, it returns `None`.
- **Code Snippet:**
    ```python
    def get_max(self):
        if self._heap_size > 0:
            return self._arr[0]
        return None
    ```

#### Get Min (MinHeap)
- **Description:** Retrieves the minimum element from the heap without removing it. This operation is crucial in min-heap applications where the smallest element needs to be accessed quickly and frequently, such as in priority queue implementations. It returns the root of the heap, which is the smallest element, with a time complexity of O(1). If the heap is empty, it returns `None`.
- **Code Snippet:**
    ```python
    def get_min(self):
        if self._heap_size > 0:
            return self._arr[0]
        return None
    ```
These methods enhance the functionality of heap data structures by providing efficient access to the most critical elements (maximum or minimum) depending on the type of heap implemented. Both `get_max` and `get_min` play pivotal roles in various algorithmic processes where heaps are used, ensuring optimal performance and immediate data retrieval.
#### Feature 10: Increase/Decrease Key
#### Increase Key (MaxHeap)
- **Description:** Modifies the value of an element within the MaxHeap by increasing its key, ensuring that the heap maintains its max-heap property afterward. This method is crucial when the priority of an element increases and it needs to be adjusted within the heap. The element is first updated to the new higher value, and then a `bubble up` operation is performed to relocate the element to its appropriate position in the heap.
- **Code Snippet:**
    ```python
    def increase_key(self, heap_index, newVal):
        self._arr[heap_index] = newVal
        self._bubble_up(heap_index)
    ```

#### Decrease Key (MinHeap)
- **Description:** Alters the value of an element within the MinHeap by decreasing its key, and then ensures the min-heap property is maintained. This operation is used when the priority of an element is reduced and it might need to move deeper into the heap to maintain the heap integrity. The element is updated to the new lower value followed by a `bubble up` operation to adjust the element to its new correct position.
- **Code Snippet:**
    ```python
    def decrease_key(self, heap_index, newVal):
        self._arr[heap_index] = newVal
        self._bubble_up(heap_index)
    ```
### CSV Data Handler

#### Overview
The `CSVDataHandler` class provides functionality to interact with CSV files specifically tailored to handle numerical data for applications dealing with heap and stack data structures. It supports writing to and reading from CSV files, ensuring data integrity through a validation decorator.

#### Constructor
- **Description:** Initializes the `CSVDataHandler` with a default or specified filename.
- **Code Snippet:**
    ```python
    def __init__(self, filename='output.csv'):
        self.filename = filename
    ```

#### Feature 1: Write Numbers to CSV (Heap)
- **Description:** Writes an array of numbers representing a heap structure into a CSV file. The numbers are written in a way that represents the level order traversal of a binary tree, where each level is written in a new row.
- **Code Snippet:**
    ```python
    def write_numbers_to_csv_heap(self, numbers):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            index = 0
            count = 1
            while index < len(numbers):
                next_row = numbers[index:index + count]
                writer.writerow(next_row)
                index += count
                count *= 2
    ```

#### Feature 2: Write Numbers to CSV (Stack)
- **Description:** Writes a list of numbers representing a stack structure into a CSV file. Each element of the stack is written in a separate row.
- **Code Snippet:**
    ```python
    def write_numbers_to_csv_stack(self, stack):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for item in stack:
                writer.writerow([item])
    ```

#### Feature 3: Read Numbers from CSV
- **Description:** Reads numbers from a CSV file and returns them as a list. This method ensures that all values retrieved are numeric, leveraging a decorator to validate data integrity.
- **Code Snippet:**
    ```python
    def read_numbers_from_csv(self):
        rows = self.__read_rows_from_csv()
        numbers = []
        for row in rows:
            numbers.extend([int(num) for num in row])
        return numbers
    ```

#### Feature 4: Clear CSV
- **Description:** Clears all data from the CSV file, effectively resetting it.
- **Code Snippet:**
    ```python
    def clear_csv(self):
        open(self.filename, 'w').close()
    ```

### Decorator Design Pattern in `CSVDataHandler`

#### Validation Decorator
- **Purpose:** The validation decorator (`__validate_numbers`) is used to wrap the internal method that reads rows from the CSV file. It ensures that every value read from the file is a valid digit, raising a `ValueError` if non-numeric data is encountered. This pattern enhances function capability by adding a layer of data validation without modifying the core functionality of the data reading process.
- **Implementation:**
    ```python
    @staticmethod
    def __validate_numbers(func):
        def wrapper(self, *args, **kwargs):
            rows = func(self, *args, **kwargs)
            for row in rows:
                for num in row:
                    if not str(num).isdigit():
                        raise ValueError(f"Found a non-numeric value: '{num}'")
            return rows
        return wrapper
    ```

This documentation provides a comprehensive overview of `CSVDataHandler` functionalities, explaining how data is managed in CSV format for both heap and stack structures. The inclusion of a validation decorator demonstrates the use of the decorator design pattern to add functionality maintainably.

### CommandInvoker Class Overview

#### Description
The `CommandInvoker` class plays a crucial role in handling commands in an application. It acts as the central point through which all user commands pass, executing and undoing them as needed. By employing the Singleton design pattern, it ensures that there is only one instance of `CommandInvoker` throughout the application, maintaining a consistent state across various components that might need to invoke commands. The command classes themselves are a perfect example of the principle of Abstraction, their functionality is apparent just from the method signature, and doesn't require any further knowledge to adopt.

#### Singleton Design Pattern
- **Purpose:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it which is useful since we want a single command interface. This is achieved in the `CommandInvoker` class using a custom metaclass, `SingletonMeta`, which controls instance creation.
- **Implementation:**
    ```python
    class SingletonMeta(type):
        _instances = {}

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]
    ```

#### Command Design Pattern
- **Purpose:** The Command pattern encapsulates a request as an object, thereby allowing users to parameterize clients with queues, requests, and operations. It supports undoable operations and logs changes so that they can be replayed or reversed.
- **Invoker Role:** In this pattern, `CommandInvoker` acts as the invoker that stores and executes commands. It can execute new commands, undo previous commands, and print a history of operations.

#### Class Functions

##### Execute Command
- **Description:** Executes a command object, stores it in the command history, and logs its description for later review. Encapsulation is present with the command history list which is a private attribute that is only accessible within its own class. 
- **Code Snippet:**
    ```python
    def execute_command(self, command):
        command.execute()
        self.__history.append(command)
        self.__description_history.append(command.description())
    ```

##### Undo Command
- **Description:** Reverses the last command executed, if there are any commands in the history. It also logs the undo operation.
- **Code Snippet:**
    ```python
    def undo_command(self):
        if self.__history:
            self.__description_history.append("Undid an action.")
            command = self.__history.pop()
            command.undo()
        else:
            print("No commands to undo")
    ```

##### Print History
- **Description:** Prints all executed command descriptions, providing a clear trace of user actions and system responses.
- **Code Snippet:**
    ```python
    def print_history(self):
        print("Command History:")
        for command_description in self.__description_history:
            print(command_description)
    ```

#### Application Integration
The `CommandInvoker` is used in any system where commands are part of the user interaction, especially in GUI or CLI menu interfaces. This structure allows the system to handle complex sequences of user commands efficiently, providing features like command history tracking and the ability to undo actions.
In your command pattern setup, abstract methods play a crucial role in enforcing a standard interface for all command objects within the system. Below is an explanation suitable for your coursework report, formatted in Markdown, detailing the use and implementation of abstract methods in your command classes.

### 

### Overview of Abstract Methods in Command Classes

Abstract methods are a key feature in Python's Abstract Base Classes (ABCs). They are methods that are declared in the abstract class but are not implemented. Concrete classes that inherit from the abstract class are required to implement these methods, providing specific functionalities. This enforces a contract for these classes, ensuring a consistent interface across different implementations.

### Purpose of Abstract Methods in Command Pattern

In the context of the Command design pattern, abstract methods define a blueprint for command execution and reversal (undoing a command). This pattern requires each command to have a predictable behavior and interface, allowing the commands to be used interchangeably within the system.

#### Code Implementation of Abstract Methods

Here's how abstract methods are declared using Python's `abc` module, which provides the infrastructure for defining Abstract Base Classes.

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command. This method must be implemented by any subclass."""
        pass

    @abstractmethod
    def undo(self):
        """Reverses the execution of the command. This method must be implemented by any subclass."""
        pass
```

### Implementation in Concrete Command Classes

Each concrete command class must implement the `execute` and `undo` methods. These implementations define how the command affects the application state and how these effects can be reversed.

#### Example: ExportHeapToCSVCommand

- **Purpose:** Handles the exporting of heap data to a CSV file.
- **Execute Method:**
    ```python
    def execute(self):
        self.backup = self.handler.read_numbers_from_csv()  # Backup existing data
        self.handler.write_numbers_to_csv_heap(self.numbers)  # Write new data to CSV
    ```
- **Undo Method:**
    ```python
    def undo(self):
        self.handler.write_numbers_to_csv_heap(self.backup)  # Restore the CSV from the backup
    ```
- **Description Method:**
    ```python
    def description(self):
        return f"ExportHeapToCSV executed with data: {self.numbers}"
    ```

Using abstract methods in the command classes ensures that each command adheres to a standard interface, promoting a robust, scalable, and maintainable codebase in applications that implement the Command design pattern.


## Results and Summary


## Results

- **Implementation of Design Patterns:** Successfully implemented three design patterns—Singleton, Decorator, and Command—which significantly enhanced the functionality and robustness of the program. These patterns facilitated the management of application state and extended the capabilities of user command processing.
- **Application of OOP Principles:** Applied all four pillars of Object-Oriented Programming—encapsulation, abstraction, inheritance, and polymorphism—making the program robust and maintainable. This approach helped in structuring the program into clear, modular components that are easier to manage and extend.
- **File Operations with CSV Files:** Integrated comprehensive file operations for reading from and writing to CSV files, which enabled effective data storage and manipulation, demonstrating practical file handling and data processing within the program.

## Conclusions

This coursework has provided a deep dive into the fundamentals of Python, including basic syntax and advanced applications such as Object-Oriented Programming and design patterns. Through this project, I have achieved:
- **A Robust Application Framework:** The use of design patterns and OOP principles has resulted in a robust, maintainable program structure that can efficiently handle complex data manipulations and user interactions.
- **Practical Implementation Skills:** Gained practical experience in implementing file operations with CSV files, enhancing the program's ability to manage external data effectively.
- **Future Prospects:** The program offers a solid foundation for future enhancements, including the potential addition of a real-time updating interface and further detailed data processing features. This groundwork sets the stage for possible expansions, such as incorporating graphical user interfaces or extending functionality to handle additional data types or operations.
