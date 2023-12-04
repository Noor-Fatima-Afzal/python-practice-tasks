a = [[1, 2, 3],
     [4, 5, 6],
     [1, 3, 3]]
ans = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        ans[j][i] = a[i][j]

for r in ans:
    print(r)
