class Student:
    # defining constructor for Student class
    # 'self' parameter is a reference to the current instance of the class and used to access variables that belong to the class
    # 'self' argument must always be passed in constructor
    # there are 2 types of constructors, default and parameterized
    # that constructor will be called with whom the parameters are matched 
    
    # there are 2 types of attributes -> class attribute and object attribute
    # class attribute
    school = "Zilla School" # class attribute is common for all students
    
    # this is default constructor
    def __int__(self):
        print("Default constructor called")
        
    # this is parameterized constructor
    def __init__(self, name, marks):  
        # print(self) # print(s1) and print(self) gives the same output because 'self' is pointing at the same object which is created under this class
        # in 'self.name', name is called an attribute
        self.name = name # object attribute is different for all student
        # in 'self.marks', marks is called an attribute
        self.marks = marks
        print("adding new student in database...")
        

s1 = Student("Shafayat Tazoar", 98) # the constructor is automatically called when an object is created
# print(s1) # self and s1 are the same thing, self is pointing at s1 currently
print(s1.name, s1.marks)

s2 = Student("Iron Man", 97)
print(s2.name, s2.marks)