a=str(input("enter a number"))
def count_13(b):
    count1=0
    count3=0
    for character in a:
        if character=="1":
            count1+=1
        if character=="3":
            count3+=1 
    b=(count1,count3)  
    print(b) 

count_13(a)    


