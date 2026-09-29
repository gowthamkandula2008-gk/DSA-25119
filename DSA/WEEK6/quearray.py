queue = []
n = int(input("Enter the number of elements: "))

# Enqueue
print("Enter the elements:")
for i in range(n):
    value = int(input())
    queue.append(value)

print("Queue after insertion:", queue)

# Dequeue
if len(queue) > 0:
    removed = queue.pop(0)
    print("Deleted element:", removed)
else:
    print("Queue is empty")

# Display
print("Queue after deletion:", queue)

# Peek
if len(queue) > 0:
    print("Front element:", queue[0])
else:
    print("Queue is empty")