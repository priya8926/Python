# def sum(x):
#     return x + 10

def fun(x , y):
    return 10+x(y)

sum = lambda x: x+10
cube = lambda x: x*x*x
avg = lambda x , y : (x+y)/2

print(sum(1))
print(cube(2))
print(avg(5,7))
# print(fun(cube,2))
print(fun(lambda x : x*x*x , 2) )