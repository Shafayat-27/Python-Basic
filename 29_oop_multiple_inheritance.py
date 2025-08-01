class First:
    def __init__(self, first):
        self.first = first
    
    def printFirst(self):
        return self.first
        
class Second:
    def __init__(self, second):
        self.second = second
        
    def printSecond(self):
        return self.second

class FullName(First, Second):
    def __init__(self, first, second):
        First.__init__(self, first)
        Second.__init__(self, second)
    
    def printName(self):
        fullname = self.printFirst()+" "+self.printSecond()
        print(fullname)

fullName = FullName("Emma", "Watson")
fullName.printName()