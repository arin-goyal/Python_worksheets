def even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]  # List comprehension to filter even numbers
    return even_numbers

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = even_numbers(sample_list)
print("Even numbers from the given list:", result)