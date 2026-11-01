class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self):
        value = int(input("Enter element: "))
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print("Element inserted.")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Deleted element:", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front
            print("Queue elements:")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

# Main program
queue = Queue()
while True:
    print("\n--- QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        queue.enqueue()
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.peek()
    elif choice == 4:
        queue.display()
    elif choice == 5:
        print("Program exited.")
        break
    else:
        print("Invalid choice.")
