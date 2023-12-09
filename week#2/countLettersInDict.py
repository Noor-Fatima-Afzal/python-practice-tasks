string="noor fatima"
count={}
for letter in string:
    if letter in count:
        count[letter]+=1
    else:
        count[letter]=1
print(count)