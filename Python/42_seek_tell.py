# seek() and tell() function are used to work with file objects and theire position within a file

# with open("file.txt" , "r") as f:
#     print(type(f))
#     # move to the 10th byte in the file
#     f.seek(7)

#     # read the next 5 bytes
#     print(f.tell())
#     data = f.read(10)
#     print(data)

with open ("samle.txt" , "w") as f:
    f.write("Hello World!")
    f.truncate(5)

with open("samle.txt" , "r") as f:
    print(f.read())