s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)   # s1 ma s2 ni value avi jay
print(s1 , s2)

# Symmetric differen => ae value je common nathi
s3 = s1.symmetric_difference(s2)
print(s3)

s3 = s1.difference(s2) # s1 ma value hoy ane s2 ma nai hoy
print(s3)

# isdisjoint() =>banne ma kai pan common nai hoy
print(s2.isdisjoint(s1))

print(s1.issuperset(s2))

#  add items
s1.add(6)
print(s1)

# remove items
s1.remove(1)
print(s1)

s1.discard(1)
print(s1)

item = s1.pop()
print(s1)
print(item)

# del s2 # delete entire set
# s2.clear() # only remove elements not set



