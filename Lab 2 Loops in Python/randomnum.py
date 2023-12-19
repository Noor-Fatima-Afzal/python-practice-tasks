import random
hiddenNumber=random.randint(1,100)
userGuuess=0
while userGuuess!=hiddenNumber:
    userGuuess==int(input("Guess a number: "))
    if userGuuess > hiddenNumber and userGuuess <=hiddenNumber+5:
        print("close to hidden number but still high! ")
    elif userGuuess > hiddenNumber:
        print("number is too much high!")
    elif userGuuess < hiddenNumber and userGuuess >=hiddenNumber-5:
        print("close to hidden number but still low! ")
    elif userGuuess < hiddenNumber: 
        print("number is too much low!")
    else:
        print("that's right!")    
              
