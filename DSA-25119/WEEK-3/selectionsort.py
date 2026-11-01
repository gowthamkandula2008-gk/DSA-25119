def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        smallest = i

        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j

        arr[i], arr[smallest] = arr[smallest], arr[i]


n = int(input("Enter the number of elements: "))

arr = []

for _ in range(n):
    arr.append(int(input("Enter the element: ")))

print("Before sorting:", arr)

selection_sort(arr)

print("After sorting:", arr)