'''def quicksort(a, low, high):
    if low < high:
        i = low + 1
        j = high
        pivot = low

        while i <= j:
            while i <= high and a[i] <= a[pivot]:
                i += 1

            while a[j] > a[pivot]:
                j -= 1

            if i < j:
                a[i], a[j] = a[j], a[i]

        # Put pivot in its correct position
        a[pivot], a[j] = a[j], a[pivot]

        quicksort(a, low, j - 1)
        quicksort(a, j + 1, high)


a = list(map(int, input("Enter numbers to sort: ").split()))

n = len(a)
quicksort(a, 0, n - 1)

print("Sorted array:", a)'''

def quicksort(a, low, high):
    # Continue sorting only if there are at least two elements
    if low < high:

        # i starts from the element after the pivot
        i = low + 1

        # j starts from the last element
        j = high

        # Select the first element as the pivot
        pivot = low
        
        while i <= j:


            while i <= high and a[i] <= a[pivot]:
                i += 1


            while a[j] > a[pivot]:
                j -= 1

            # If i and j have not crossed, swap the elements
            if i < j:
                a[i], a[j] = a[j], a[i]

        # Place the pivot in its correct position
        a[pivot], a[j] = a[j], a[pivot]

        # Recursively sort the left part
        quicksort(a, low, j - 1)

        # Recursively sort the right part
        quicksort(a, j + 1, high)


# Read numbers from the user and convert them into a list of integers
a = list(map(int, input("Enter numbers to sort: ").split()))
n = len(a)
quicksort(a, 0, n - 1)

# Display the sorted array
print("Sorted array:", a)