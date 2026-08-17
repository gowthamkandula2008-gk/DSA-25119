def selection_sort(arr):  # #SelectionSort
    n = len(arr)

    for i in range(n - 1):  # #SelectPosition
        min_index = i

        for j in range(i + 1, n):  # #FindMinimum
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]  # #SwapElements

    return arr  # #ReturnSortedArray


# Taking input
n = int(input("Enter no of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

print("Sorted array:", selection_sort(arr))
