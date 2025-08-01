# del keyword is used for deleting any object or object attribute

class Student:
    def __init__(self, name):
        self.name=name
    
s1 = Student("Emma")
print(s1)
del s1
print(s1)