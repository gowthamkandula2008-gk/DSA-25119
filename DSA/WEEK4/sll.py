class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # i. Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            value = int(input("Enter value: "))
            self.insert_end(value)

    # ii. Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
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
        current.next = new_node

    # v. Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            print("Value not found")
        else:
            current.next = current.next.next

    # vi. Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # vii. Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

    # viii. Count number of nodes
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
            print(current.data, end=" -> ")
            current = current.next

        print("None")


linked_list = LinkedList()

while True:

    print("\n----- SINGLY LINKED LIST -----")
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
        linked_list.create()

    elif choice == 2:
        value = int(input("Enter value: "))
        linked_list.insert_beginning(value)

    elif choice == 3:
        value = int(input("Enter value: "))
        linked_list.insert_end(value)

    elif choice == 4:
        value = int(input("Enter value: "))
        index = int(input("Enter index: "))
        linked_list.insert_at_index(value, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        linked_list.delete_by_value(value)

    elif choice == 6:
        linked_list.delete_beginning()

    elif choice == 7:
        linked_list.delete_end()

    elif choice == 8:
        print("Number of nodes:", linked_list.count_nodes())

    elif choice == 9:
        linked_list.display()

    elif choice == 10:
        print("Program exited.")
        break

    else:
        print("Invalid choice")
