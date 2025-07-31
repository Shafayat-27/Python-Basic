# methods in oop are functions that belongs to object
# basically those functions who are defined inside a class are called methods

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        
    def printName(self):
        print("Hello, ", self.name)
        
    def getMarks(self):
        print("Your obtained mark is", self.mark)
        
s1 = Student("Emma", 32)
s1.printName()
s1.getMarks()