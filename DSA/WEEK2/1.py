def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#taking input 
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

target = int(input("Enter element to search: "))

result = linear_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
