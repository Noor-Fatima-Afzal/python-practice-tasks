num=int(input("enter a number"))
for i in range(num):
    for j in range(num-i-1):
        print(" " , end="")
    for k in range(i+1):
        print("*" , end=" ")   
    print()         