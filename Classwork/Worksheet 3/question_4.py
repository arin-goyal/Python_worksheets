def count(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    # Display the counts
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")

# Example usage
input_string = input("Enter a string: ")
count(input_string)
