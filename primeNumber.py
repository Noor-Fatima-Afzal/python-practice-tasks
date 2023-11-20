x=int(input("enter a number"))
if x==1:
      print(x, "is not a prime number")
else:         

    for i in range(2,x):
        if x%i==0:
            print("it is not a prime number")
            break
    else:
        print("it is not a prime number")  
        