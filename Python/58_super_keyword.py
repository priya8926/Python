#  it is used to refred parent class
# class parent:
#     def parent_class(self):
#         print("this is parent class method")
    
# class child(parent):
#     def parent_class(self):
#         print("priya")
#         super().parent_class()
#     def child_class(self):
#         print("this is child class method")
#         super().parent_class()

# child_obj = child()
# child_obj.child_class()
# child_obj.parent_class()

class employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self, name , id , lang):
        super().__init__(name , id)
        self.lang = lang

priya = employee('priya' , "21")
payal = programmer('payal', "20" , "python")
print(priya.name)
print(payal.id)
print(payal.lang)
print(payal.name)