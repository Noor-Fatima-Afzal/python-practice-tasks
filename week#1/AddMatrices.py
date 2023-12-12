# a=[[1,2,3],
#    [4,5,6],
#    [1,3,3]]
# b=[[1,2,3],
#    [4,5,6],
#    [1,2,3]]
m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix1 = []; columns = []
for i in range(0,m):
  matrix1 += [0]
for j in range (0,n):
  columns += [0]
for i in range (0,m):
  matrix1[i] = columns
for i in range (0,m):
  for j in range (0,n):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix1[i][j] = int(input())
a=matrix1   

m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix2 = []; columns = []
for i in range(0,m):
  matrix2 += [0]
for j in range (0,n):
  columns += [0]
for i in range (0,m):
  matrix2[i] = columns
for i in range (0,m):
  for j in range (0,n):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix2[i][j] = int(input())
b=matrix2 

ans=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range (len(a)):
    for j in range (len(a)):
        ans[i][j]=a[i][j]+b[i][j]
for r in ans:
    print(r)        

