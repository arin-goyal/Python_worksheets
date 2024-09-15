# Generate a 3*4*6 3D whose each elemnt is *
array_3d = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

# print the 3D array
for layer in array_3d:
    for row in layer:
        print(row)
    print()