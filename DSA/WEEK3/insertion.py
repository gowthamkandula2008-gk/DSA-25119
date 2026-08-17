def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):  # #SelectElement
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:  # #CompareAndShift
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key  # #InsertInCorrectPosition

    return arr  # #ReturnSortedArray


# Taking input
n = int(input("Enter no of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))  # #TakeInput

print("Sorted array:", insertion_sort(arr))  # #DisplayResult
