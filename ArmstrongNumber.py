lower=int(input("enter lower number"))
uper=int(input("enter uper number"))
for num in range(lower,uper+1):
    numstr = str(num)
    num_digits = len(numstr)
    sum=0
    temp=num
    while temp > 0:
        remainder=temp%10
        base=remainder**num_digits
        sum=sum+base
        temp=temp//10
    if sum==num:
        print(sum,"is is an armstrong number")
    