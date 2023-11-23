punc='!@#$%^&8*(,.><?/)'
string=input("enter a string here:")
empty_string=""
for i in string:
    if i not in punc:
        empty_string=empty_string+i
print(empty_string)        