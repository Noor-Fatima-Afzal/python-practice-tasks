num=int(input("enter a number"))
if num<0:
    print("factorial is not possible")
elif num==0:
    print("factorial is 1")   
else:
    for i in range(1,num):
        num=num*i
        i=i+1
    print("factorial is" ,num)    
    
