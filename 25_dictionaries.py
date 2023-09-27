info = {
    "priya" :"human being",
    "spoon" : "object",
    344 : "payal",
    598 : "jay"
}
print(info["priya"])
print(info[344])

# Accessing dictionary items

print(info)
print(info["spoon"])
print(info[598])
print(info.get('priya'))
print(info.get('priya2'))
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"the value corresponding to the key {key} is{info[key]}")

print(info.items())
for key,value in info.items():
    print(f"The value corresponding to the key{key} is {value}")