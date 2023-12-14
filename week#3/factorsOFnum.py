num=int(input("enter a number"))
factors=list()
for i in range(2,num):
    if num%i==0:
        factors.append(i)
factors.insert(0,1)        
print(factors)
