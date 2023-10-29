class employee:
#     def __init__(self):
#         self.name = "priya"

# a = employee()
# print(a.name)

    def __init__(self):
        self.__name = "priya"

a = employee()
# print(a.__name) # can not be accessed directly
print(a._employee__name)