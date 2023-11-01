class Animal:

    def __init__(self,name,species):
       self.name = name
       self.species = species

    def make_sound(self):
        print("sound made by animal")

class Dog(Animal):
    def __init__(self , name , breed ):
        Animal.__init__(self , name, species= "Dog")
        self.breed = breed

    def make_sound(self):
        print("bakrk !!!")

d = Dog("dog" , "man")
d.make_sound()

a = Animal("cat " , "man")
a.make_sound()


