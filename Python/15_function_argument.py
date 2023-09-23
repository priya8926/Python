def avg(*numbers):
    # print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum +i
    print("avg is " , sum/len(numbers))

avg(5,5)

def name(**name):
    print("hello" , name['fname'] , name['mname'] , name['lname'])

name(fname="priya"  , mname = "vijaybhai" , lname="patel")