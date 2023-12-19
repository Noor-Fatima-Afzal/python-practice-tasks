num = int(input("Enter the number of rows for the triangular pattern: "))
for i in range(1, num+1):
    row = '*' * (2*i - 1)
    print(row.center(2*num - 1))

num1 = int(input("Enter the number of rows for the triangular pattern: "))
for i in range(1, num1+1):
    for j in range(num1-i-1):
        print(" " , end="")
    for j in range (i+1):
        print("*",end=" ") 
    print()
