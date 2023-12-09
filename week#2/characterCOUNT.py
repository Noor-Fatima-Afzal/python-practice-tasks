count=0
mylist=["this is the first string", "this is the 2nd string"]
for string in mylist:
    for character in string:
        if character=="z":
            count=count+1
print(count)