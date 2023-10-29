class A:
    companyName = "Goggle" # class variable 
    noOfEmployee = 0
    def __init__(self ,  name):
        self.name = name
        self.raise_amount = 0.2 #instancce variable
        A.noOfEmployee += 1 

    def details(self):
        print(f"the name of the person is {self.name} and raise amount of {self.noOfEmployee} sized {self.companyName} company is {self.raise_amount}")

emp1 = A("priya")
emp1.raise_amount = 0.3 #instancce variable
# A.details(emp1)
emp1.companyName = "Samsung"
emp1.details()

A.companyName = "Apple"

emp2 = A("sandhya")
emp2.details()
# emp2.companyName = "microsoft"

emp3 = A("diya")
emp3.details()
