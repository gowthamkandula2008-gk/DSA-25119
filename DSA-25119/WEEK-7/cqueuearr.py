class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue overflow")
            return
        
        if self.front == -1:
            self.front = 0
    
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"{data} is added to queue")

    def dequeue(self):
        if self.front == -1:
            print("Queue underflow")
            return
            
        print(f"{self.queue[self.front]} is deleted from queue")
        self.queue[self.front] = None
    
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.front == -1:
            print("No elements in the queue")
        else:
            print(self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Empty Queue")
            return
        temp = self.front
        while True:
            print(self.queue[temp], end=" -> ")
            if temp == self.rear:
                break
            temp = (temp + 1) % self.size
        print("None")

q = CircularQueue(5)
while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            e = int(input("Enter element to add: "))
            q.enqueue(e)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.display()
        elif choice == 5:
            break
        else:
            print("Choose a valid choice")
    except ValueError:
        print("Please enter a valid number")