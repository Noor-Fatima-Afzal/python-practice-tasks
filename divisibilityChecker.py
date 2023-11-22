num=int(input("divisibility by what number you want to check?"))
print("the numbers divisible by",num,"are")
divisible_numbers=list()
for i in range (1 , 100):
    if i%num==0:
        divisible_numbers.append(i)
print(divisible_numbers)

