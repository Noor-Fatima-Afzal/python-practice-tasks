def add_lists(list1, list2):
    return [i + j for i, j in zip(list1, list2)]

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = add_lists(list1, list2)
print("Sum of corresponding elements:", result)