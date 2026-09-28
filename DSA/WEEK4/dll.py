class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # i. Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for _ in range(n):
            value = int(input("Enter value: "))
            self.insert_end(value)

    # ii. Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    # iii. Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    # iv. Insert at specific index
    def insert_at_index(self, value, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_beginning(value)
            return

        current = self.head

        for _ in range(index - 1):
            if current is None:
                print("Index out of range")
                return
            current = current.next

        if current is None:
            print("Index out of range")
            return

        new_node = Node(value)

        new_node.next = current.next
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node

        current.next = new_node

    # v. Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while current and current.data != value:
            current = current.next

        if current is None:
            print("Value not found")
            return

        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next is not None:
            current.next.prev = current.prev

    # vi. Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    # vii. Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while current.next:
            current = current.next

        if current.prev is None:
            self.head = None
        else:
            current.prev.next = None

    # viii. Count nodes
    def count_nodes(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    # ix. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


dll = DoublyLinkedList()

while True:

    print("\n----- DOUBLY LINKED LIST -----")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete at beginning")
    print("7. Delete at end")
    print("8. Count nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()

    elif choice == 2:
        value = int(input("Enter value: "))
        dll.insert_beginning(value)

    elif choice == 3:
        value = int(input("Enter value: "))
        dll.insert_end(value)

    elif choice == 4:
        value = int(input("Enter value: "))
        index = int(input("Enter index: "))
        dll.insert_at_index(value, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        dll.delete_by_value(value)

    elif choice == 6:
        dll.delete_beginning()

    elif choice == 7:
        dll.delete_end()

    elif choice == 8:
        print("Number of nodes:", dll.count_nodes())

    elif choice == 9:
        dll.display()

    elif choice == 10:
        print("Program exited.")
        break

    else:
        print("Invalid choice")
