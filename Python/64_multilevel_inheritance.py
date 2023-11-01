class Animal:
    def __init__(self , name , voice):
        self.name = name
        self.voice = voice

    def show(self):
        print(f"name : {self.name}")
        print(f"voice : {self.voice}")

class Dog(Animal):
    def __init__(self , name , breed):
        Animal.__init__(self, name, voice="Woof")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"breed : {self.breed}")
class color(Dog):
    def __init__(self , name , color):
        Dog.__init__(self , name , breed="golden")
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"Color : {self.color}")

obj = color("Tommy" , "Brown")
obj.show()
print(color.mro())