import os
# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")

#  to rename
# for i in range(0,100):
#     os.rename(f"data/Day{i+1}" , f"data/Tutorial{i+1}")


#  to search folder
folders = os.listdir("data")

for f in folders:
    print(f)
    print(os.listdir(f"data/{f}"))
