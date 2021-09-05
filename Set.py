"""
s = set()
print(type(s))

l = [10,20,30,40,50]
s_from_list = set(l)
print(s_from_list)
"""

# s = set()
# s.add(19)
# s.add(29)
# s.add(39)
# s.add(49)
# print(s)

# s1 = s.union({19,30,39,47})
# print(s,s1)

# s2 = s.intersection({19,30,39,47})
# print(s,s2)

# print(len(s2))
# print(max(s2))
# print(min(s2))

# s3 = {78,45,66,71}
# print(s1.isdisjoint(s3))

# s.remove(39)
# print(s)


# s = {56,78,34,9,3,2,10}
# print(s)
# print(type(s))


# Important : This syntax will created an empty dictionary and not an empty set

# a = {}
# print(type(a))

# An empty set can be created using the below syntax :

b = set()
print(type(b))

b.add(45)
b.add(78)
b.add(22)
# b.add([78,4,89,32]) # List not adding in set cz list is unhashable
# b.add({10:20}) # Dict not adding in set cz dict is unhashable
b.add((12,34,43,56)) # Tuple can be added in set

print(b)

b.pop()
b.pop()
print(b)
