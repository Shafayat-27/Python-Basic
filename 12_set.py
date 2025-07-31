# set must be unique, if duplicate values are given, set ignores the duplicates
# set is immutable, that's why list and dictionary cannot be stored inside a set
# set is unordered

collection = {1, 2, 2, 2, "hello", "world", "world", 4}
print(collection)
print(type(collection))

# if you want to declare an empty set you may thing you should write like this
empty = {} 
print(type(empty)) # this is printing its type as dictionary
# so you need to do it like this
empty2 = set()
print(type(empty2))

#***Some Methods of Set***#
# add method adds elements to the set
empty2.add(1)
empty2.add(2)
empty2.add(3)
print(empty2)

# remove method
empty2.remove(1) # removes value 1 from the set
print(empty2)

# clear the full set
print(len(empty2))
empty2.clear()
print(empty2)

# removes any random value or element from the set
empty3 = {1, 3, 5, 7, 9}
empty3.pop()
print(empty3)

# union of set, selects unique values and create a new set, i does not change old sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# intersection, combines common values and returns new
print(set1.intersection(set2))