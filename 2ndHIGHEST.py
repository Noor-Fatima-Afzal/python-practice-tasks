n=int(input("enter number of students"))
name_array=[]
score_array=[]
for i in range(n):
    name = input("enter name of student")
    score = float(input("enter score of student"))
    name_array.append(name)
    score_array.append(score)
sndHighest=sorted(set(score_array))[1]
result=[]
for i in range(n):
    if score_array[i]==sndHighest:
        result.append(name_array[i])
result.sort()
l=len(result)
for i in range (l):
    print(result[i]) 