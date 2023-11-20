num=int(input("enter a number"))
num_str = str(num)
num_digits = len(num_str)
sum=0
temp=num
while temp > 0:
    remainder=temp%10
    base=remainder**num_digits
    sum=sum+base
    temp=temp//10
if sum==num:
    print("is is an armstrong number")
else:
    print("not an armstrong number")
