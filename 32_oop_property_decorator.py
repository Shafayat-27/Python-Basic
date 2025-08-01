# case: 1
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # This is a fixed value assigned at the time of object creation. That's why it does not update itself when something is changed.
        self.percentage = str((self.phy+self.chem+self.math)/3) + "%"
        
s1 = Student(97, 98, 99)
print(s1.percentage)
# suppose s1 did not get get 97 in physics, it should be 86.
# change physics number
s1.phy = 86
print("Physics marks changed to", s1.phy)
# but the percentage did not changed automatically
print("But the percentage did not changed automatically. It is still:", s1.percentage)

# case: 2
# we use the @property decorator in any method in he class to use the method as a property
class Student1:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    # @property decorator makes the 'percentage' method as a attribute of this object and changes according to need
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"
        
stu = Student1(97, 98, 99)
print(stu.percentage)
stu.phy = 86
print("Physics marks changed to", stu.phy)
print("Percentage is:", stu.percentage) # percentage is not method, it became attribute 