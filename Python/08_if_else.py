# age = int(input("Enter your age : "))
# print("your age is " , age)
#
# if(age>18):
#     print("you can drive")
#     print("yes")
# else:
#     print("you can not drive")
#     print("no")
# print("i am out of loop")

# else if
# a = int(input("enter number : "))
# print("your number is " , a)
# if(a>0):
#     print("number is positive")
# elif(a==0):
#     print("number is zero")
# else:
#     print("number is negative")

# nested if
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
