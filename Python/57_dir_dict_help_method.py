# dir() function  returns a list of all the attributes and methos avalaible for an object
x= [1,2,3]
# print(dir(x))
# print(x.__add__)

# the dct attributes returns a dictinory representaion of an object's attributes

class person:
    def __init__(self, name , age):
        self.name = name 
        self.age = age

p = person("priya" , 21)
print(p.__dict__)

#  the help() function is used to get help documentation for an object , including a description and methods

print(help(person))