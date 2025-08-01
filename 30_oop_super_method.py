# super() method is used to access attributes and methods of the parent class

class Car:
    @staticmethod
    def start():
        print("Car starting.....")
        
    def __init__(self, type):
        self.type = type

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()
        
c1 = ToyotaCar("Prius", "Electric")
print(c1.name)
print(c1.type)