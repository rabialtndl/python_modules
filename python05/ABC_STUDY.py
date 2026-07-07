#Abstract class : A class cannot be instantiated on its own; meant to be subclassed.
#                They can contain abstract methods, which are declared but have no implementation.
#                Abstract clasess benefits: 
#                1. Prevents instatntion of the class itself
#                2. Requires children to use inheritedabstract methods.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("You can ride the car :)")
        
    def stop(self):
        print("You have to stop the car!!!")
        
car = Car()
car.go()
car.stop()
