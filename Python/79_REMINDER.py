import time
from plyer import notification

time_hour = float(input("set the hours after you want to drink water"))
while(True):
    time.sleep(time_hour)
    notification.notify(title = "reminder " , message = "You  should drink water" , timeout = 2)