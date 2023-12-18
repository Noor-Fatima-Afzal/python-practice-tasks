num = int(input("Enter a number: "))
for i in range(1, num+1):
    for j in range(1, num+1-i):
        print("*", end="")
    print()

num = int(input("Enter a number: "))
for i in range(num+1,0,-1):
    for j in range(1, num+1-i):
        print("*", end="")
    print()


