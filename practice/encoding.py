dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}
a=list(dic.keys())
b=list(dic.values())
lis=['GFEDC'] #it should print 1 2 and 3 only
for string in lis:
    for character in string:
        index=a.index(character)
        print(b[index])
dic["occupation"]="engineer"  
print(dic)      

