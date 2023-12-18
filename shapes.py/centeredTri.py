num = int(input("Enter the number of rows for the triangular pattern: "))
for i in range(1, num+1):
    row = '*' * (2*i - 1)
    print(row.center(2*num - 1))
