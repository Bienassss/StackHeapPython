from data_structures import *
from command_logger import *
from file_parser import *

csv_handler = CSVDataHandler('my_numbers.csv')
invoker = CommandInvoker()
stack = Stack()
heap = MinHeap(50)

def main_menu():
    print("\nAvailable Operations:")
    print("1. Stack Operations")
    print("2. Heap Operations")
    print("3. CSV File Operations")
    print("4. Undo Last Command")
    print("5. Print Command History")
    print("0. Exit")
    choice = input("Select an operation: ")
    return choice

def stack_operations(stack):
    while True:
        print("\nStack Operations:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Print stack array")
        print("0. Return to Main Menu")
        choice = input("Choose an operation: ")

        if choice == '1':
            element = input("Enter an element to push: ")
            command = PushCommand(stack, element)
            invoker.execute_command(command)

        elif choice == '2':
            if not stack:
                print("Stack is empty!")
            else:
                command = PopCommand(stack)
                invoker.execute_command(command)

        elif choice == '3':
            command = PrintStackArrayCommand(stack)
            invoker.execute_command(command)

        elif choice == '0':
            break

        else:
            print("Invalid choice")

def heap_operations(heap):
    while True:
        print("\nHeap Operations:")
        print("1. Insert an element")
        print("2. Remove top element")
        print("3. Print heap array")
        print("4. Draw binary tree")
        print("0. Return to Main Menu")
        choice = input("Choose an operation: ")

        if choice == '1':
            element = input("Enter an element to insert: ")
            try:
                element = int(element)  # Convert to integer
                command = InsertKeyCommand(heap, element)
                invoker.execute_command(command)
            except ValueError:
                print("Invalid input: Please enter a valid integer.")

        elif choice == '2':
            if not heap:
                print("Heap is empty!")
            else:
                if isinstance(heap, MinHeap):
                    command = RemoveMinCommand(heap)
                else:
                    command = RemoveMaxCommand(heap)
                invoker.execute_command(command)

        elif choice == '3':
            command = PrintHeapArrayCommand(heap)
            invoker.execute_command(command)

        elif choice == '4':
            command = DrawBinaryTreeCommand(heap)
            invoker.execute_command(command)

        elif choice == '0':
            break

        else:
            print("Invalid choice")

def csv_operations():
    while True:
        print("\nCSV File Operations:")
        print("1. Import from CSV")
        print("2. Export heap to CSV")
        print("3. Export stack to CSV")
        print("4. Clear CSV")
        print("0. Return to Main Menu")
        choice = input("Choose an operation: ")

        if choice == '1':
            while True:
                print("\nSelect Import operation:")
                print("1. Import to stack")
                print("2. Import to heap")
                print("0. Return to CSV Menu")
                choice = input("Choose an operation: ")

                if choice == '1':
                    command = ImportFromCSVCommand(csv_handler, stack)
                    invoker.execute_command(command)
                    break
                elif choice == '2':
                    command = ImportFromCSVCommand(csv_handler, heap)
                    invoker.execute_command(command)
                    break
                elif choice == '0':
                    print("Returning to main menu...")
                    break 
                else:
                    print("Invalid choice, try again.")

        elif choice == '2':
            numbers = heap.return_heap_contents()
            if numbers is not None and numbers:
                command = ExportHeapToCSVCommand(csv_handler, numbers)
                invoker.execute_command(command)
            else:
                print("Heap is empty or error retrieving contents.")
                return None

        elif choice == '3':
            numbers = stack.return_stack_contents()
            if numbers:  
                command = ExportStackToCSVCommand(csv_handler, numbers)
                invoker.execute_command(command)
            else:
                print("Stack is empty or error retrieving contents.")
                return None

        elif choice == '4':
            command = ClearCSVCommand(csv_handler)
            invoker.execute_command(command)

        elif choice == '0':
            break

        else:
            print("Invalid choice")

def main():

    while True:
        choice = main_menu()
        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            command = stack_operations(stack)
        elif choice == '2':
            command = heap_operations(heap)
        elif choice == '3':
            command = csv_operations()
        elif choice == '4':
            invoker.undo_command()
            continue
        elif choice == '5':
            invoker.print_history()
            continue
        else:
            print("Invalid choice, try again.")
            continue

        if command:
            invoker.execute_command(command)

if __name__ == "__main__":
    main()
