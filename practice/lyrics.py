def lyrics_to_frequency(lyrics):
    my_dict={}
    for word in lyrics:
        if word in my_dict:
            my_dict[word]+=1
        else:
            my_dict[word]=1
    return my_dict

she_loves_you=['She', 'loves', 'you', 'yeah', 'yeah', 'yeah','She', 'loves', 'you', 'yeah', 'yeah', 'yeah','She', 'loves' ,'you', 'yeah', 'yeah', 'yeah']

new_dict=lyrics_to_frequency(she_loves_you)
print(new_dict)

def most_common_words(freq):
    values=freq.values()
    best=max(freq.values())
    words=[]
    for k in freq:
        if freq[k]==best:
            words.append(k)      
    return (words,best)
        
print(most_common_words(new_dict))   

def worrd_often(freq,min):
    result=[]
    done=False
    while not done:
        temp=most_common_words(freq)
        if temp[1]>=min:
            result.append(temp)
            for w in temp[0]:
                del(freq[w])
        else:
            done=True
    return result

print(worrd_often(new_dict,5))                

