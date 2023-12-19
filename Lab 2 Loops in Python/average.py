count=int(input("enter how many numbers"))
num=[]
for i in range(1,count+1):
    values=int(input("enter number"))
    num.append(values)
sumofnum=sum(num)
print("average is" ,sumofnum/count)