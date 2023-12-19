lis=[]
ans=[]
for i in range(1,3):
    element=int(input("enter element"))
    lis.append(element)
for i in range(len(lis)):
    if lis[i] %2 ==0:
        a="Even"
    else:
        a="Odd"    
    ans.append(a)
print(ans)    
