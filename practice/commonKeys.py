dict1 = {'a': 1, 'b': 2, 'c': 3, 'common': 10}
dict2 = {'c': 30, 'd': 4, 'e': 5, 'common': 20}
a=list(dict1.keys())
b=list(dict2.keys())
x=[]
for i in a:
    for j in b:
        if i==j:
            x.append(i)
print(x)            