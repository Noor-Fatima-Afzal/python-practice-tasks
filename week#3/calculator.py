print(".....mini calculator.....")
import math
x=float(input("enter 1st number"))
y=float(input("enter 2nd number"))
choice=input("for addition enter A, for subtration enter B, for multiplication enter M, for division enter D, for log enter L, for sin enter Sin ")
if choice=="A":
    ans=x+y
    print(ans)
elif choice=="S":
    ans=x-y
    print(ans)
elif choice=="M":
    ans=x*y
    print(ans)
elif choice=="D":
    ans=x/y
    print(ans)
elif choice=="L":     
    print("log of 1st value is ",math.log(x,10))
    print("log of 2nd value is ", math.log(y,10))
elif choice=="Sin": 
    print("sin of 1st value is ", math.sin(math.radians(int(x))))
    print("sin of 1st value is ", math.sin(math.radians(int(y))))
else:
    print("invalid operator")    

