# Without fstring
#  letter  = "my name is {} and i am from {}"
# name = "priya"
# country = "india"
# print(letter.format(name , country))

# By using fstring
name = "priya"
country ="Bharat"
print(f"My name is {name} and i am from {country}")
print(f" row fstring like this:My name is {{name}} and i am from {{country}}")

# txt = "For only {price:.3f} dollars!"
# print(txt.format(price = 49.2465454)) #return last 3 digit only

# By using fString
price = 49.562123456
txt = f"For only {price:.3f} dollars!"
print(txt)

print(f"{2*3}")