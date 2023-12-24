a = [[1, 2, 3],
     [4, 5, 6],
     [1, 3, 3]]
ans = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a)):
        ans[i][j] = a[j][i]

for r in ans:
    print(r)

result = list(zip(*[[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]))
print(result)
