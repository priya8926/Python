# a = False
# a = 7
# # print(a := True)
# print(a := 78)

# num = [1,2,3,4,5]

# while (n := len(num)) >0 :
#     print(num.pop())

# foods = list()
# while True:
#     food = input("which food do you like ? ")
#     if(food == "quit"):
#         break
#     foods.append(food)

foods = list()
while(food := input("Which food do you like?") != "quit"):
    foods.append(food)