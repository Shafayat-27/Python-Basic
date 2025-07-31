# create student class that takes name & marks of three subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def avg_mark(self):
        sum = 0
        for el in self.marks:
            sum+=el
        print("Welcome", self.name, "your average mark is", sum/3)
        
s1 = Student("Shafayat", [90, 91, 92])
s1.avg_mark()