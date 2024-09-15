# Slicing of a string

print("Slicing of a string\n")
name = "Arin Goyal"
sl_name1 = name[2:6]        # 2nd index element is not included (output = "in G")
sl_name2 = name[-8:-4]      # 2nd index element is not included (output = "in G")

print(sl_name1)
print(sl_name2)

sl_name3 = name[3:]     # [x:] this blank = length
sl_name4 = name[:3]     # [:x] this blank = 0
sl_name5 = name[:]      # [:] from 0 to length

print(sl_name3)
print(sl_name4)
print(sl_name5)

# Slicing with skip value

print("\nSlicing with skip value\n")

mystr = "0123456789"
s1_mystr = mystr[0:9:3]       # Starts with 1st value till the 2nd value(not included), skips (3rd-1) elements

print(s1_mystr,"\n")