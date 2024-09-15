def difference(n):

  if n > 17:
    return 2 * abs(n - 17)
  else:
    return abs(n - 17)

num = int(input("Enter a number: "))

result = difference(num)
print("The difference is:", result)