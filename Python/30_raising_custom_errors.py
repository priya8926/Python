a = input("Enter any value between 5 and 9: ")
if int(a) < 5 or int(a) > 9:
    raise ValueError("Value should be between 5 and 9")
elif a == "quit":
    print("Error")
else:
    print("Code ended successfully")
