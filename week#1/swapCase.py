def swap_case(s):
    sequence=list(s)
    for i in range(len(sequence)):
        if sequence[i].islower():
            sequence[i]=sequence[i].upper()
        elif sequence[i].isupper():
            sequence[i]=sequence[i].lower()   
    return str(''.join(sequence))
if __name__ == '__main__':
    s = input("enter a string which you want to swap")
    result = swap_case(s)
    print(result)