lis=["Noor","fAtima","aFzal"]
ans=[]
for string in lis:
    for character in string:
        if character.isupper():
            ans.append(character)
print(ans)        