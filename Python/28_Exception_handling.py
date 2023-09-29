# a = input("enter the number: ")
# print(f"Multiolication table of {a} is : ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# # except Exception as e:
#         # print(e)
# except:
#     print("Invalid Input")

# print("some lines")
# print("end")

try:
    num= int(input("enter an integer: "))
    print(num)
except ValueError:
    print("not an integer")