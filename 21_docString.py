# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
    ''' take in number n , return the square n'''  # it is not a comment it is docString
    print(n**2)
square(5)
print(square.__doc__)