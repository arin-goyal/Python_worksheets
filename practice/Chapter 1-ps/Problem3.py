import os

# Specify the direcctory path you want to list
directory_path = '/C'

# Get the contents of the current directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
