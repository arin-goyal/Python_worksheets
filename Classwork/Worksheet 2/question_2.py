# Program to sum all the items in a list without using any inbuilt functions
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

# Example list
L = [1, 2, 3, 4, 5]

# Calculate the sum
result = sum_list(L)
print("The sum of all items in the list is:", result)