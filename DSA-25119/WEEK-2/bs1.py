def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter the element: ")))

target = int(input("Enter the search element: "))

# Sort the unsorted array
arr.sort()

print("Sorted array:", arr)

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")