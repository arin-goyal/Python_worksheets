def distinct_elements(input_list):
    distinct_list = []
    
    for item in input_list:
        if item not in distinct_list:
            distinct_list.append(item)

    return distinct_list

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
new_list = distinct_elements(input_list)
print("List with distinct elements:", new_list)
