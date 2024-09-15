def within_range(number):

  return (100 <= number <= 1000) or (number == 2000)

num = int(input("Enter a number: "))

if within_range(num):
  print("The number is within the specified range.")
else:
  print("The number is not within the specified range.")