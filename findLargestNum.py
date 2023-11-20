x=float(input("eter 1st number"))
y=float(input("eter 2nd number"))
z=float(input("eter 3rd number"))

if x>y:
    if x>z:
        print(x,"is the largest number")
elif y>x:
    if y>z:
        print(y,"is the largest number")
else:
    print(z,"is the largest number")        
