def countdown(n):
    if n == 0:
        print("launch")
        return

    print(n)
    countdown(n-1)


n = int(input("Enter the number: "))
countdown(n)