def square_elements(input_list):
    new_list = [x**2 for x in input_list]
    return new_list


original_list = [1, 2, 3, 4, 5]
modified_list = square_elements(original_list)
print("Original List:", original_list)
print("Modified List (Squared):", modified_list)
