# String functions

name = "arin_goyal"

print(len(name),"\n")                   # len() function is used to get the size of string

print(name.endswith("yal"))             # String_name.endswith("abc") function tells if the string ends with abc or not
print(name.endswith("xyz"))

print("")

print(name.startswith("ari"))           # String_name.startswith("abc") function tells if the string startswith abc or not
print(name.startswith("xyz"))

print("")

print(name.count("a"))                  # String_name.count("abc") function tells if the string ends with abc or not

print("")

print(name.capitalize())                # Capitalize the first character and lowercase the rest
print(name.upper())                     # Capitalize all the characters
print(name.lower())                     # Lowercase all the characters
print(name.title())                     # Capitalize first letter of every word and lowercase the rest

print("")

print(name.find("goyal"))               # Finds a word and return index of first occurence of that word
print(name.replace("goyal","arin"))     # Replace the first word with second in the entire string