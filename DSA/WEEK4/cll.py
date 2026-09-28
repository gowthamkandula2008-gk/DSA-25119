class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # i. Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for _ in range(n):
            value = int(input("Enter value: "))
            self.insert_end(value)

    # ii. Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    # iii. Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    # iv. Insert at specific index
    def insert_at_index(self, value, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_beginning(value)
            return

        if self.head is None:
            print("Index out of range")
            return

        current = self.head
        position = 0

        while position < index - 1 and current != self.tail:
            current = current.next
            position += 1

        if position != index - 1:
            print("Index out of range")
            return

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

        if current == self.tail:
            self.tail = new_node

    # v. Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = self.tail

        while True:
            if current.data == value:
                break

            previous = current
            current = current.next

            if current == self.head:
                print("Value not found")
                return

        # Only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        # Delete head
        if current == self.head:
            self.head = self.head.next
            self.tail.next = self.head
            return

        # Delete other node
        previous.next = current.next

        # Delete tail
        if current == self.tail:
            self.tail = previous

    # vi. Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    # vii. Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current = self.head

        while current.next != self.tail:
            current = current.next

        current.next = self.head
        self.tail = current

    # viii. Count nodes
    def count_nodes(self):
        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:
            count += 1
            current = current.next

            if current == self.head:
                break

        return count

    # ix. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(Head)")

    # x. Display head and tail
    def display_head_tail(self):
        if self.head is None:
            print("List is empty")
            return

        print("Head:", self.head.data)
        print("Tail:", self.tail.data)
        print("Tail points to:", self.tail.next.data)


cll = CircularLinkedList()

while True:

    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete at beginning")
    print("7. Delete at end")
    print("8. Count nodes")
    print("9. Display / Traverse")
    print("10. Display Head and Tail")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        value = int(input("Enter value: "))
        cll.insert_beginning(value)

    elif choice == 3:
        value = int(input("Enter value: "))
        cll.insert_end(value)

    elif choice == 4:
        value = int(input("Enter value: "))
        index = int(input("Enter index: "))
        cll.insert_at_index(value, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        cll.delete_by_value(value)

    elif choice == 6:
        cll.delete_beginning()

    elif choice == 7:
        cll.delete_end()

    elif choice == 8:
        print("Number of nodes:", cll.count_nodes())

    elif choice == 9:
        cll.display()

    elif choice == 10:
        cll.display_head_tail()

    elif choice == 11:
        print("Program exited.")
        break

    else:
        print("Invalid choice")
