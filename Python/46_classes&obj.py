class person:
    name = "priya"
    age = 21
    city = "navsari"
    def info(self): # self means jena mate aa object call thay
        print(f"{self.name}'s age is {self.age} and her city is {self.city}")

a = person()
b = person()
b.name = "diya"
a.name = "payal"
print(a.name)
a.info()
b.info()