def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        if target < numbers[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1


n = int(input("Enter the number of elements: "))

numbers = []

for _ in range(n):
    value = int(input("Enter the element: "))
    numbers.append(value)

target = int(input("Enter the search element: "))

position = binary_search(numbers, target)
print(position)