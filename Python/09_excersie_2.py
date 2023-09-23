import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
# timestamp = input(time.strftime('%H'))
# print(timestamp)
# timestamp = input(time.strftime('%M'))
# print(timestamp)
# timestamp = input(time.strftime('%S'))
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

# hour = input(time.strftime('%H'))
hour = int(input("enter hour in 24 hour format : "))
if (hour >= 5 & hour < 12):
    print("good morning sir..")
elif (hour >= 12 & hour < 16):
    print("good afternoon sir")
elif (hour >= 16 & hour < 20):
    print("good evening sir")
else:
    print("good night sir...")
