class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # Push operation
    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
        self.count += 1

        print(value, "pushed into stack")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return

        value = self.top.data
        self.top = self.top.next
        self.count -= 1

        print("Popped element:", value)

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Count operation
    def count_nodes(self):
        print("Number of elements:", self.count)

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current = self.top

        print("Stack elements:")

        while current:
            print(current.data)
            current = current.next


stack = Stack()

while True:

    print("\n----- STACK USING LINKED LIST -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Count")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.push(value)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.count_nodes()

    elif choice == 5:
        stack.display()

    elif choice == 6:
        print("Program exited.")
        break

    else:
        print("Invalid choice")
