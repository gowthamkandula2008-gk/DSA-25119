def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


n = int(input("Enter the number of elements: "))

arr = []

for _ in range(n):
    arr.append(int(input("Enter the element: ")))

print("Before sorting:", arr)

bubble_sort(arr)

print("After sorting:", arr)