# a built-in data type that lets us create immutable sequence of values
tup = () #empty tuple
print(tup)
print(type(tup))

# if you have 1 element, then you should give a comma after it
tup1 = (1, )
print(tup1)
print(type(tup1))
# otherwise it will be treated as an integer, float or string depending on its type
tup2 = (1)
print(tup2)
print(type(tup2))

# for multiple valued tuple, comma is not mandatory, it will be treated like a tuple anyway
tup3 = (1, 2, 3, 4)
print(tup3)
print(type(tup3))

# element access
print(tup3[0])

# slicing in tuple works same as list
print(tup3[0:3])

#tuple methods
print(tup3.index(2)) #prints the index of element 2's first occurrence
print(tup3.count(2)) #prints how many times 2 is there
