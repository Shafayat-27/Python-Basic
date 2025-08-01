#              Private(like) attributes and methods               #
#-----------------------------------------------------------------#
# private attributes and methods are only meant to be used only within the class and are not accessible from outside the class

class Student:
    def __init__(self, name, mobile):
        self.name = name
        self.__mobile = mobile # double underscore makes it private attribute
        
    def getMobile(self):
        print(self.__mobile) # only accessible within the class
    
    def __getName(self): # double underscore makes it private method
        print(self.name)
        
    def welcome(self): # only accessible within the class
        self.__getName()
    
s1 = Student("Emma", 12345)
print(s1.name)
# print(s1.mobile) # this will give error as mobile attribute is private
s1.getMobile()
# print(s1.__getName) # this will give error as __getname is private method
s1.welcome()
        