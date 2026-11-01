def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"

    if num == 0:
        return 1

    return num * factorial(num - 1)


n = int(input("Enter a number: "))

result = factorial(n)
print("Factorial =", result)