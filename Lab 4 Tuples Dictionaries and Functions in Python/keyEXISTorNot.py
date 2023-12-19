dict={
    '1':2,
    '5':"noor",
    '3':1,
}
key_value=input("enter key")
if key_value in dict.keys():
    print(True)
    print("key=",key_value)
    print("value=",dict[key_value])
else:
    print(False)    