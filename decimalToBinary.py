num=int(input("enter a decimal number"))
l=list()
while num>0:
    rem=num%2
    l.append(rem)
    num=num//2
l.reverse()
for i in l:
    print(i ,end=" ")