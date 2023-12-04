def count_substring(string, sub_string):
    count=0
    for x in range(0, len(string)):
        if string[x:x + len(sub_string)] == sub_string:
            count = count + 1 
    return(count)

if __name__ == '__main__':
    string = input("enter string").strip()
    sub_string = input("enter sub-string").strip()
    
    count = count_substring(string, sub_string)
    print(count)