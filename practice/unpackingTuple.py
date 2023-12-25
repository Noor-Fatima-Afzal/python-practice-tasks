#aliasing
warm=[1,2,3,4]
hot=warm
hot.append(5)
print(hot)
print(warm)

#cloning
cool=[1,2,3]
chill=cool[:]
chill.append(5)
print(cool)
print(chill)

#sort return kuch nahi krta
warm=[5,3,1,5,2]
sortedlist=warm.sort()
print(warm)
print(sortedlist)

#sorted orignal mai changing nahi krta
warm=[5,3,1,5,2]
sortedlist=sorted(warm)
print(warm)
print(sortedlist)

# l1=[1,2,3,4]
# l2=[l1]
# l3=[5]
# l4=[l2,l3]
# print(l4)
# l3.append(6)
# print(l4)

def remve_dup(l1,l2):
    l1_copy=l1[:]
    for i in l1_copy:
        if i in l2:
            l1.remove(i)
l1=[1,2,3,4]
l2=[1,2,6,7]
print(remve_dup(l1,l2))

l=['A',2,3,4]
l.extend(["s","wj"])
print(l)
l[2]=l[2]+1
print(l)
a=4
print(l[a-4])
