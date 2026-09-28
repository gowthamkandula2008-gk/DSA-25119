def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


n = int(input("Enter the number of elements: "))

arr = []

for _ in range(n):
    arr.append(int(input("Enter the element: ")))

print("Before sorting:", arr)

sorted_arr = merge_sort(arr)

print("After sorting:", sorted_arr)
