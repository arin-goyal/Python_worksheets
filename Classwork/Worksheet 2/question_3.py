# Program to multiply all the items in a list without using any inbuilt functions
def mul_list(lst):
    total = 1
    for item in lst:
        total *= item
    return total

# Example list
L = [1, 2, 3, 4, 5]

# Calculate the multiplication
result = mul_list(L)
print("The multiplication of all items in the list is:", result)