queue = []

# Enqueue operation
def enqueue():
    value = int(input("Enter element: "))
    queue.append(value)
    print("Element inserted.")

# Dequeue operation
def dequeue():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Deleted element:", queue.pop(0))

# Peek operation
def peek():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element:", queue[0])

# Display operation
def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue elements:")
        for element in queue:
            print(element, end=" ")
        print()

# Main program
while True:
    print("\n--- QUEUE USING ARRAY ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program exited.")
        break
    else:
        print("Invalid choice.")
