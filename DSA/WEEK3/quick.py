def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = []
    greater = []

    for value in arr[:-1]:
        if value <= pivot:
            smaller.append(value)
        else:
            greater.append(value)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


n = int(input("Enter the number of elements: "))

arr = []

for _ in range(n):
    arr.append(int(input("Enter the element: ")))

print("Before sorting:", arr)

sorted_arr = quick_sort(arr)

print("After sorting:", sorted_arr)
