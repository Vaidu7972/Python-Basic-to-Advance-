# OOP : Object Oriented Programing

# OOP 4 pillors: Abstraction 
#                Encapsulation
#                Inheritance
#                Polymorphism 

 
# Abstraction:

"""
Hiding the implementation details of a class
and showing only essential features to the user.
Example: Car (we know how break works but dont knoe their exact function/mechanism.)
"""

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
    print("Car started...")
    
# Object creation (outside the class)
car1 = Car()
car1.start()
print("\n")

# Encapsulation  

"""
Data + Function = Capsule  (single unit called object)
"""

class Car:   
    def __init__(self):
        self.speed = 0                # private variable

    def accelerate(self):
        self.speed = 60
        print("Car is moving")

    def show_speed(self):
        print("Speed:", self.speed)
 
car1 = Car()
car1.accelerate()
car1.show_speed()
print("\n")

# del Keyword
"""
used to delete object proprties or object itself
Syntax : del s1.name
         del s1
"""   

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Vaidehi")                             # Creating object (outside the class)
print(s1.name,"\n")                                      # Printing object data

del s1                                              # Deleting object

# print(s1.name)                                      # Gives error



#function inside a class. 

class Account:                               #Class
    def __init__(self,accno,accpass):        #Constructor
        self.accno=accno                     #Instance Variables
        self.accpass=accpass

    def resetpass(self):                     #Method :function inside a class.                  
        print(self.accpass)

acc1=Account("123","abc")                    #Object
print(acc1.accno)
print(acc1.accpass)
print(acc1.resetpass)

        
# Private (like) Attribute & Method
"""
used only within class and  not accessable from outside the class (private)like above ex.
private members are created using double underscore __ before the name.
They are not accessible directly from outside the class.
"""

class Person:
    __name="Vaidehi"              #__name is a private attribute.

    def __hello(self):         #__hello() is a private method.
        print("hello")

    def welcome(self):         #welcome() is a public method. It accesses the private method inside the class. This is the correct way to use private members.
        self.__hello()

p1=Person()
print(p1.welcome())            #print : none  #Encapsulation 

"""
p1.welcome() calls the private method internally.
welcome() prints "hello".
Since welcome() does not return anything, it returns None.
print() displays None.
"""  


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self,amount):
        self.balance -= amount
        print("RS.", amount,"was debited" )
        print("total balance = ",self.get_balance())
        
    def credit(self,amount):
        self.balance += amount
        print("RS.", amount,"was credited" )
        print("total balance = ",self.get_balance())
        
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)    
        
        
        



