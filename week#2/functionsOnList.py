fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#counting
print(fruits.count('apple'))

#appending
fruits.append("kiwi")
print(fruits)

#find index
a=fruits.index('banana')
print(a)

#reverse
fruits.reverse()
print(fruits)

#sorting
fruits.sort()
print(fruits)

#poping
popped_fruit =fruits.pop()
print(f"Popped fruit: {popped_fruit}")
print(f"Remaining fruits: {fruits}")

