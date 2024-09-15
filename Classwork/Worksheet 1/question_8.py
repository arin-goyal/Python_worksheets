num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

num1, num2 = num2, num1
num1 += 1

print(f"After swapping and incrementing:")
print(f"First number (originally second number) + 1: {num1}")
print(f"Second number (originally first number): {num2}")