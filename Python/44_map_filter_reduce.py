#  map method line by line excute kare 
# MAP
def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,3,4,5,6,7,8,9]
# newl = []
# for item in l:
#     newl.append(cube(item))
newl = list(map(cube ,l))

print(newl)

# FILTER
def filter_fun(a):
    return a>5

newnewl = list(filter(filter_fun , l))
print(newnewl)

# REDUCE
from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y , numbers)
print(sum)