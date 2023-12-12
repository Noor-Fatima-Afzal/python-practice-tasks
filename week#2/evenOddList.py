def even_odd_status(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

input_numbers = list(map(int, input("Enter 20 numbers separated by space: ").split()))

result_list = [even_odd_status(num) for num in input_numbers]

print(result_list)
