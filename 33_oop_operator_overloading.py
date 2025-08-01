# Polymorphism -> this means "many forms". One good example of polymorphism is operator overloading. When the same operator is allowed to have different meaning according to the context that is called operator overloading.

# implicit operator overloading
print(1+2) # means addition of two numbers
print("Emma" + " Watson") # means concatenation of two strings
print([1, 2, 3]+[4, 5, 6]) # means merging of two lists

# explicit operator overloading
# A dunder function (short for double underscore) in Python is a special method with names that start and end with double underscores, like __init__, __str__, __len__, etc. These are also called magic methods or special methods. They let you define how your object behaves with built-in operations.

# | **Operator** | **Meaning**               | **Dunder (Magic) Function** |
# | ------------ | ------------------------- | --------------------------- |
# | `+`          | Addition                  | `__add__(self, other)`      |
# | `-`          | Subtraction               | `__sub__(self, other)`      |
# | `*`          | Multiplication            | `__mul__(self, other)`      |
# | `/`          | Division                  | `__truediv__(self, other)`  |
# | `//`         | Floor Division            | `__floordiv__(self, other)` |
# | `%`          | Modulus (Remainder)       | `__mod__(self, other)`      |
# | `**`         | Exponentiation            | `__pow__(self, other)`      |
# | `==`         | Equal to                  | `__eq__(self, other)`       |
# | `!=`         | Not equal to              | `__ne__(self, other)`       |
# | `<`          | Less than                 | `__lt__(self, other)`       |
# | `<=`         | Less than or equal to     | `__le__(self, other)`       |
# | `>`          | Greater than              | `__gt__(self, other)`       |
# | `>=`         | Greater than or equal to  | `__ge__(self, other)`       |
# | `len()`      | Length                    | `__len__(self)`             |
# | `str()`      | String representation     | `__str__(self)`             |
# | `repr()`     | Official representation   | `__repr__(self)`            |
# | `[]`         | Indexing                  | `__getitem__(self, key)`    |
# | `in`         | Membership check          | `__contains__(self, item)`  |
# | `()`         | Callable (like functions) | `__call__(self, ...)`       |
# | `int(obj)`   | Convert to integer        | `__int__(self)`             |
# | `float(obj)` | Convert to float          | `__float__(self)`           |
# | `del obj`    | Deletion                  | `__del__(self)`             |

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def showComplex(self):
        print(self.real,"+",self.imag,"j")
        
    def __add__(self, other):
        newReal = self.real + other.real
        newImag = self.imag + other.imag
        return Complex(newReal, newImag)
        
num1 = Complex(1, 3)
num1.showComplex()
num2 = Complex(2, 6)
num2.showComplex()

num3 = num1 + num2
num3.showComplex()