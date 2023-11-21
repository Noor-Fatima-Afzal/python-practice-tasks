s=int(input("enter you salery"))
g=int(input("enter you scale"))
if g>16:
    sal=s+((40/100)*s)
    print(sal)
elif g<=16:
    sal = s + ((20 / 100)*s)
    print(sal)
