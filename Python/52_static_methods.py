class math:
    def __init__(self , num):
        self.num = num
    
    def addtonum(self, n):
        self.num = self.num+n

    @staticmethod # self lagavani jarur nai pde
    def sum(a,b):
        return a+b

a = math(5)
print(a.num)
a.addtonum(3)
print(a.num)
print(a.sum(10,20))
# print(math.sum(10,20))