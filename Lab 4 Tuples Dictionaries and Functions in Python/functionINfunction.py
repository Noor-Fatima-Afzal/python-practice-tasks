def  max(x, y):
    if x>y:
        return x
    if y>x:
        return y
    
def cube(z):
    return z**3

x=int(input("enter 1st num"))
y=int(input("enter 2nd num"))
print(cube(max(x, y)))    
