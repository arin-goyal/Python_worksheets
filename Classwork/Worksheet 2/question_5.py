D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# (i) Add new entry in D; key=8 and value is 8.8
D[8] = 8.8
print("After adding key=8, value=8.8:", D,"\n")

# (ii) Remove key=2
if 2 in D:
    del D[2]
print("After removing key=2:", D,"\n")

# (iii) Check whether 6 key is present in D
if 6 in D:
    print("Key=6 is present in D.\n")
else:
    print("Key=6 is not present in D.\n")

# (iv) Count the number of elements present in D
count = len(D)
print("Number of elements present in D:", count,"\n")

# (v) Add all the values present in D
total_sum = 0
for value in D.values():
    total_sum += value
print("Sum of all values in D:", total_sum,"\n")

# (vi) Update the value of key=3 to 7.1
if 3 in D:
    D[3] = 7.1
print("After updating key=3 to 7.1:", D,"\n")

# (vii) Clear the dictionary
D.clear()
print("After clearing the dictionary:", D,"\n")