def func():
    try:
        l = [12,54,1654,532]
        i = int(input("enter an index : "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
 
    finally: 
        print("i am always here")

x = func()
print(x)