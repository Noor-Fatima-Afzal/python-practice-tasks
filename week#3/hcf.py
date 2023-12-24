def findHCF(x,y):
    if x>y:
        smallest=y
    else:
        smallest=x
    for i in range(1, smallest+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
def findLCM(x,y):
    if x>y:
        greatest=x
    else:
        greatest=y
    while(True):
       if((greatest % x == 0) and (greatest % y == 0)):
           lcm = greatest
           break
       greatest += 1

    return lcm       


a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
hcf=findHCF(a,b)
# print("the lcm is",findLCM(a,b))
lcm = (a * b) // hcf
print(lcm)
    