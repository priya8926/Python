class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    @classmethod
    def formstring(cls , string):
        return cls(string.split("-")[0] , int(string.split("-")[1]))

e1=  Employee("priya" , 25000)
print(e1.name)
print(e1.salary)

string = "payal-25000"
e2 =  Employee.formstring(string)
print(e2.name)
print(e2.salary)

class person:
    def __init__(self , name , age):
        self.name  = name
        self.age = age

    @classmethod
    def from_string(cls,string):
        name , age = string.split(",")
        return cls(name , int(age))

person  = person.from_string('priya patel, 30' )
print(person.name , person.age)