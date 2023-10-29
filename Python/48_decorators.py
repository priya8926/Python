def greet(fx):
    def mfx(*args , **kwargs):
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx
@greet
def hello():
    print("hello")

def add(a, b):
    return (a+b)

hello()