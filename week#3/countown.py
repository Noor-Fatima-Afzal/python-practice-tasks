a=int(input("enter a number"))
def count_down(a):
    if a>0:
        for i in range (a,0,-1):
             result=i
             print(result)
        else:
            result="countdown is stopped"     
    return result
print(count_down(a))