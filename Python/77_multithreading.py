import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

#  normal code
# func(4)
# func(3)
# func(2)

# same code using thread 
time1 = time.perf_counter()
t1 = threading.Thread(target=func , args= [4])
t2 = threading.Thread(target=func , args= [3])
t3 = threading.Thread(target=func , args= [2])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()
print(time2 - time1)