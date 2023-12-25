dict1 = {'a': 1, 'b': 2, 'c': 3, 'common': 10}
dict2 = {'c': 30, 'd': 4, 'e': 5, 'common': 20}

merged={}
for key,value in dict1.items():
    if key in merged:
        merged[key]+=value
    else:
        merged[key]=value

for key,value in dict2.items():
    if key in merged:
        merged[key]+=value
    else:
        merged[key]=value
        
print(merged)        