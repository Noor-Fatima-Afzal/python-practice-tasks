#agr tuple k ander list pari hoi hai tu ussy change kia jaa skta hai
#lkn tuple ko change nahi kia jaa skta
t=(["sdhjh","jhdjh"],)
# t=list(t)
t[0][0]="n"
print(t)

lis=[1,2,3,4]
lis2=[9]
dic={'a':2,'b':5}
#by whole dict
lis.extend(dic.items())
#by dic keys
lis.extend(dic.keys())
#by dic values
lis.extend(dic.values())
#by lis in argument
lis.extend([3,3,1,1,1])
#by lis as variable 
lis.extend(lis2)
print(lis)

#insert
lis2.insert(0,"hjhjh")
print(lis2)

#append
lis2.append(dic.keys())
print(lis2)
cubes=[]
sum=0
for i in range(3):
    cubes.append(i**3)
    sum+=i**3
print(sum)

#remove
#the first 1 in the list
lis.remove(1)
print(lis)

#pop
print(lis2.pop(2))
print(lis2)

#clear but it clears==del it removes or deletes list
lis2.clear()
# del lis2
print(lis2)

#count
print(lis.count(1))

#reverse (takes no argument)
a="python"
a=list(a)
a.reverse()
print(a)

#copy
b=a.copy()
a.reverse()
print(a)

#sort kuch b return nahi krta is liye none aye ga
x=[4,5,6,1,2,3]
l=x.sort()
print(l)
x.sort()
print(x)

#sorted
x=["hsj","aoehjh","kiwe","bks"]
sorted_x=sorted(x)
print(sorted_x)

dic={1:"noor",2:"jsk",9:"sjhj"}
print(dic.get(1,"not found"))
dic[2]="noor"
print(dic)

l1=[1,2,4,9]
l2=[8,1,2,4]
#making dic from 2 lists
ans=dict(zip(l1,l2))
print(ans)
#adding 2 lists
sum1=[]
for x,y in zip(l1,l2):
    ans=y-x
    sum1.append(ans)
print(sum1)


print(sorted({1: 'D', 24: 'B', 3: 'B', 19: 'E', 5: 'A'}))

tuple=('b','w','a','k','d','c')
sortedlist=sorted(tuple)
sortedtuple=tuple(sortedlist)
print(sortedtuple)