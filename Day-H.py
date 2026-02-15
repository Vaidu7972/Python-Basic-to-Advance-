#  Inheritance
"""When one class (child/derived) is derives properties & methods of another class (parent/base)"""
class Car:                                  #base class
    color = "black"
    @staticmethod                        # decorator 
    def start():
        print("car Started...")
        
    @staticmethod
    def stop():       
        print("car Stopped...")    
        
class ToyotaCar(Car):                    #derived class
    def __init__(self, name):        #__init__ is a constructor    
        self.name = name
        
car1 = ToyotaCar("fortuner")                                        
car2 = ToyotaCar("prius")

print(car1.name)      
print(car1.start())
print(car1.color)