# Static Methods -> methods that don't use the self parameter (works at class level)
# When we don't need a function for any object, we just deal with it in class level. Means that we don't need to add the 'self' parameter in that method. So, we write '@staticmethod' before defining that method. '@staticmethod' is called a decorator. 

# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

class Student:
    @staticmethod # -> this is called a decorator
    def college():
        print("abc")