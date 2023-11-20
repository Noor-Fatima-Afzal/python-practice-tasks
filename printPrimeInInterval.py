import random
num=  random.randint(1,100)
print(num)

if num==1:
    print("it is not a prime number")
else:
    for  i in range  (2,num):
        if num%i==0:
            print("it is not a prime number") 
            break
    else:
         print("it is a prime number")  

