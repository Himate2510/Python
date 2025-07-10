def lenlist(li):
    if li==[]:
        return 0
    else:
        return 1+lenlist(li[1:])
li = [1, 2, 3, 4, 5]
print("Length of the list is: ", lenlist(li))