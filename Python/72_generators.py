# yeild pele thi value store ni kare
def my_generator():
    for i in range(500):
        yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)