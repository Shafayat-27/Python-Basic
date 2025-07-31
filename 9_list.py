# list stores values of different data types, it it mutable
myList = [10, 20, 'hello', 'world', 30, 40, 50]
print(myList)

# list is mutable
myList[0] = 'nation'
print(myList)

# string is immutable
# str = 'hello'
# str[0] = 'y' # this will give an error

# list slicing
print(myList[0:4])
print(myList[:4])
print(myList[-4:-1])

# list methods
newList = [7, 6, 55, 14, 30, 2, 1]
newList.append(8)
print(newList)
newList.sort()
print(newList)
newList.sort(reverse = True)
print(newList)
newList.reverse()
print(newList)
newList.insert(2, 10)
print(newList)
newList.remove(1) #removes first occurrence of the element
print(newList)
newList.pop(1) #remove index number 1's element
print(newList)