# Input string
input_string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

# Group size
group_size = 4

# Iterate through the string and print in groups
for i in range(0, len(input_string), group_size):
    group = input_string[i:i + group_size]
    print(group)
