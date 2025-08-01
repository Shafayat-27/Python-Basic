# a class method is bound to the class and receives the class as an implicit first argument
# class method is another type of decorator
# note: static method can't access or modify class state and generally for utility

# if you try to change the class attribute's(name) value by doing similar code as below, it won't change. Because this code creates another object attribute 'name' and sets the value to it. 
class Student1:
    name = "anonymous"
    def changeName(self, name):
        self.name = name
        
s1 = Student1() 
s1.changeName("Emma") # you set name = Emma but this change is meant for the particular object
print(s1.name) 
print(Student1.name) # this prints 'anonymous', which means the class attribute 'name''s value is not changed
    
# there are three ways to change class attributes
# Way 1
class Student2:
    name = "anonymous"
    def changeName2(self, name):
        Student2.name = name # writing this line makes it happen
        
s2 = Student2() 
s2.changeName2("Emma")
print(s2.name) 
print(Student2.name)

# Way 2
class Student3:
    name = "anonymous"
    def changeName3(self, name):
        self.__class__.name = name
        
s3 = Student3() 
s3.changeName3("Emma")
print(s3.name) 
print(Student3.name)

# Way 3: class method
class Student4:
    name = "anonymous"
    @classmethod
    def changeName4(cls, name):
        cls.name = name
        
s4 = Student4() 
s4.changeName4("Emma")
print(s4.name) 
print(Student4.name)

# we have three types of functions/methods
# 1. static method -> does not have class or self parameter
# 2. class method -> have class parameters, used to access class attributes
# 3. normal method -> have self parameter, used to access object attributes