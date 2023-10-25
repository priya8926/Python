# READING A FILE

# f = open("myfile.txt" , "r")
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

f = open("myfile2.txt" , "w")
f.write("hiii this is myfile2 directory")
f.close()

with open("myfile2.txt", "w") as f:
    f.write("okkk")
