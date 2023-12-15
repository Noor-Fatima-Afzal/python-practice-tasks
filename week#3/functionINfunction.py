def  max(x, y):
    if x>y:
        return x
    if y>x:
        return y
    
def cube(z):
    return z**3

x=5
y=2

#function within function
print(cube(max(x, y)))    
