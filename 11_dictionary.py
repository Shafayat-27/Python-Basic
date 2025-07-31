# dictionary is unordered, mutable, don't allow duplicate keys
dict = {
    "name": "Shafayat",
    "age": 25,
    "isAdult" : True,
    "favorite_movies" : ["A", "B", "C"],
    "scores": (10, 20, 30, 40),
    "subject":{
        "english" : 80,
        "physics" : 90,
        "math" : 94
    }
}

print(dict)
print(type(dict))
print(dict["name"])
print(dict["subject"]["math"])

# ***Some Methods of Dictionary***
# returns all the keys
print(dict.keys())
# type cast into list
print(list(dict.keys()))
# print length of the list
print(len(list(dict.keys())))

# returns all the values
print(dict.values())

# returns all key-value pairs in a dictionary
print(dict.items())
pairs = list(dict.items())
print(pairs[0])

# return value for a key
print(dict["name"]) #Shafayat
print(dict.get("name")) #Shafayat
# then what is the difference if two of them giving the same outcome
# print(dict["name2"]) # gives error
# print(dict.get("name2")) #returns 'none'

# update the old dictionary
newDict = {
    "city": "dhaka",
}
dict.update(newDict)
print(dict)