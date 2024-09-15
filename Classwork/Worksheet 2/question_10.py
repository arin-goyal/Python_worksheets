# Program to check if a given number is even or odd
def check_even_odd(number):
    is_even = (number % 2 == 0)
    is_odd = not is_even
    
    if is_even:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


number = int(input("Enter a number: "))
check_even_odd(number)
