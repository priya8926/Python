#  existing class ne extend karva 
class employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id

    def show(self):
        print(f"the name of employee : {self.name} and id is : {self.id}")

class prog(employee):
    def showlan(self):
        print("python")

class lan(prog):
    def compiler(self):
        print("vscode")

e1 = employee("priya" ,2608)
e2 = prog("piya" ,2609)
e1.show()
e2.show()
e2.showlan()
e3 = lan("cdbf" , 665)
e3.show()
e3.showlan()
e3.compiler()