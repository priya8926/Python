tup = (1,2,79,342,32,"green", True)
# tup[0] = 90
print(type(tup) , tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 3421 in tup:
    print("yes 342 is preset in this tuple")
else:
    print("no it is not preset")
tup2 = tup[1:4] # 1 is not include
print(tup2)