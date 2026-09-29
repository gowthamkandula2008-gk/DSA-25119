class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        new=Node(data)
        if self.rear is None:
            self.front=new
            self.rear=new
        else:
            self.rear.next=new
            self.rear=new
        print(data,"Data inserted")
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp=self.front
            print(temp.data,"deleted")
            self.front=self.front.next
            if self.front is None:
                self.rear=None
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Top:",self.front.data)
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        temp=self.front
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
q=Queue()
n=int(input("Enter a number: "))
for i in range(n):
    data=int(input("Enter a number: "))
    q.enqueue(data)
q.display()
q.dequeue()
q.peek()