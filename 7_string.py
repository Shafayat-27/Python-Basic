str1 = "This is a string.\nWith a new line."
print(str1)

str2 = "This is a string with a \thorizontal tab."
print(str2)

str3 = 'This is a string with single quote.'
print(str3)

str4 = """This is a string with triple quote."""
print(str4)

# string concatenation
str5 = "Hello"
str6 = "World"
str7 = str5 + " " + str6
print(str7)

# check string length
print(len(str7))

# indexing starts from 0 in python
str8 = "Hello World"
print(str8[0])

# slicing: str[starting index : ending index], ending index is not included
print(str8[0:4])
print(str8[4:9])
print(str8[:4])
print(str8[4:])

# negative index starts from right most element and right most elements index is -1
str9 = "Apple"
print(str9[-4:-1]) # last element is not included

# string functions
str10 = "hello world"
print(str10.endswith("rld")) # returns true
print(str10.capitalize()) # capitalizes first letter
print(str10.replace("world", "CPI")) #replaces world by CPI
print(str10.find('Q')) # prints -1 because Q is not present
print(str10.find('w')) # prints 6 because w is present in the 6th index
print(str10.count('o')) # o is present 2 times
