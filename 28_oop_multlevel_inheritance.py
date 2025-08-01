class Car:
    @staticmethod
    def start():
        print("Car starting.....")
        
    @staticmethod
    def stop():
        print("Car stopping.....")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Prius(ToyotaCar):
    def __init__(self, type):
        self.type = type

c1 = Prius("Diesel")

c1.start()
print(c1.type)
c1.stop()