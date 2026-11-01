def compound_interest(principal, years):
    if years == 0:
        return 1

    return principal * compound_interest(principal, years - 1)


principal = int(input("Enter the principal growth: "))
years = int(input("Enter the number of years: "))

result = compound_interest(principal, years)
print(result)