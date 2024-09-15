input_string = input("Enter a sequence of comma-separated numbers: ")
    
number_list = [int(num) for num in input_string.split(',')]
    
number_tuple = tuple(number_list)
    
print("List:", number_list)
print("Tuple:", number_tuple)