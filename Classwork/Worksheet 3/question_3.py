def reverse_string(string):

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

string = input("Enter a string: ")

reversed_string = reverse_string(string)
print("The reversed string is:", reversed_string)