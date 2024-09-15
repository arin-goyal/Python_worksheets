principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
n = int(input("Enter the number of times interest is compounded per year: "))
time = float(input("Enter the number of years: "))

rate = rate / 100

compound_interest = principal * (1 + rate / n) ** (n * time) - principal

print(f"The compound interest is: {compound_interest:.2f}")