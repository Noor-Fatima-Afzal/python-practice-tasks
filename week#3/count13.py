
def count_13():
    count1=0
    count3=0
    string=str(input("enter number"))
    for character in string:
        if character=='1':
            count1=count1+1
        if character=='3':
            count3=count3+1
        my_tuple=(count1,count3)    
    return my_tuple        

print(count_13())
