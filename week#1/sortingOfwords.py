a=input("enter a string which you want to sort alphabetically")
a=a.casefold()
print(a)

s=a.split()
# print(s)
# for i in range(len(s)):
#     s[i]=s[i].lower()

print(s)    
s.sort()
print(s)