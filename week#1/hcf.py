def findHCF(x,y):
    if x>y:
        smallest=y
    else:
        smallest=x
    for i in range(1, smallest+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf

a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
print("the HCF is",findHCF(a,b))

    