list1 = [10, 15, 20, 25, 30, 35]
list2 = [40, 45, 50, 55, 60, 65]

new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

print("New list with odd numbers from list1 and even numbers from list2:", new_list)