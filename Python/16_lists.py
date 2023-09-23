number = [12,45,85,45,"priya"]
print(number)
print(type(number))
print(number[0])
print(number[1])
print(number[2])
# print(number[5])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)