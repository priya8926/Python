# Example of hybrid inheritance
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3( Derived1 ,  Derived2 ):
    pass

# Example of hierarchical inheritance 
class h1:
    pass

class h2(h1):
    pass

class h3(h1):
    pass

class h3(h2):
    pass