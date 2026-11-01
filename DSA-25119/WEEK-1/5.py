def fibonacci(n):
    if n < 0:
        return "Invalid input"

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")