def square_list(a):
    squared_list=[]
    for i in a:
        square_list_item=i**2
        squared_list.append(square_list_item)
    return squared_list

list=[2,3,4,5]    
print(square_list(list))