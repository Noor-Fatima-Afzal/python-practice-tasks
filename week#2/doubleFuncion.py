def double(a):
    for i in range(0,len(a)):
        a[i]=a[i]*2
    return(a)

b=['a',1,4,6,'h']
b=double(b)
print(b)