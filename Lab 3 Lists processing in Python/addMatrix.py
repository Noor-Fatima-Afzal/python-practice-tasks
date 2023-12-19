# get matrix1
matrix1=[]
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"enter element at position {i+1}, {j+1}: "))
        row.append(element)
    matrix1.append(row)
print(matrix1)
# get matrix2
matrix2=[]
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"enter element at position {i+1}, {j+1}: "))
        row.append(element)
    matrix2.append(row)
print(matrix2)

X = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
         X[i][j] = matrix1[i][j] + matrix2[i][j]
for r in X:
    print(r)
  