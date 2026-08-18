def merge_sort(arr):
    # Base condition
    if len(arr) <= 1:
        return arr

    # Divide the array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursive calls
    merge_sort(left)
    merge_sort(right)

    # Merge the two sorted arrays
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements from left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


arr = list(map(int, input("Enter numbers to sort: ").split()))

merge_sort(arr)

print("Sorted array:", arr)