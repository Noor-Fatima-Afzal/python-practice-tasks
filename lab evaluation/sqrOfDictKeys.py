my_dict = {2: 1, 3: 2, 6: 3}
print(my_dict)

#keys ki list bnai
keys=list(my_dict.keys())
print(keys)

#us list k har har element ka cube ly kar usy aik new list "cube" mai rakh diya
cube=[]
for i in keys:
    cube.append(i**3)
print(cube)

#new dict k keys mai un values ko rakh diya jo cube list k ander pari hoi thi
new_dict = {}
for i in range(len(cube)):
    new_dict[cube[i]]=my_dict[keys[i]]

print(new_dict)
     
