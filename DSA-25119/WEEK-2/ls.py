def linear_search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


n = int(input("Enter the number of elements: "))

numbers = []

for _ in range(n):
    numbers.append(int(input("Enter the element: ")))

target = int(input("Enter the search element: "))

result = linear_search(numbers, target)
print(result)