class Car:
    @staticmethod
    def start():
        print("Car starting.....")
        
    @staticmethod
    def stop():
        print("Car stopping.....")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

c1 = ToyotaCar("Prius")
c2 = ToyotaCar("Noah")

c1.start()
print(c1.name)
c1.stop()

print("\n")

c2.start()
print(c2.name)
c2.stop()
