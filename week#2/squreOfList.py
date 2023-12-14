def square(z):
    return z * z
print(list(map(square, [2, 3, 4])))

#alternative 
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)           

#alternative 
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)

#alternative 
squares2 = [x**2 for x in range(10)]
print(squares2)