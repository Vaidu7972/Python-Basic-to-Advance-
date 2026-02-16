#  Inheritance
"""When one class (child/derived) is derives properties & methods of another class (parent/base)"""
"""
Child class derives properties and methods of parent class
Types: Single Inheritance      (one child one parent)
       Multiple Inheritance    (One Base, Multiple Derived)
       Multi Level Inheritance (Multiple parent, One child)
"""
# 1.Single level Inhertance

class Car:                      # Parent / Base class: gives property to another class
    @staticmethod
    def start():
        print("Car started...")

class Toyota(Car):              # Child / Derived class: takes property from another class
    def __init__(self, name):
        self.name = name

car1 = Toyota("Fortuner")       # Creating object of child class
car1.start()                    # Creating object of child class


# OR if you want to print car name
class Car:
    def start(self):
        print("Car started...")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Car name:", self.name)

car1 = Toyota("Fortuner")
car1.start()
car1.show()
print("\n")



# 2.Multilevel

class Car:                           # Parent / Base class
    @staticmethod
    def start():
        print("Car started...")

class Toyota(Car):                   # Child / Derived class
    def __init__(self, brand):
        self.name = brand

class fortuner(Toyota):              # Child / Derived class
    def __init__(self, type):
        self.name = type

car1 = fortuner("disel")            # Creating object of child class
car1.start()  
print("\n")                     



# 3.Multiple 

class A:
    varA="class A"

class B:
    varB="class B" 

class C(A,B):
    varC="class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
print("\n")


#Super Method

"""
 we can call it parent class in inheritance.
 it is used to accress methods of the parent class from the child class.
When a child class wants to use something from its parent class, it uses super().

To reuse parent class code.
To avoid rewriting same code.
To extend parent class functionality.
Useful in inheritance.
"""

# Parent Class 
class Animal:                          # Animal is the parent class.
    def sound(self):
        print("Animals make sound")

# Child Class
class Dog(Animal):                     # Dog is the child class.
    def sound(self):
        super().sound()                # calling parent class method. "Call the parent class method first."
        print("Dog barks")             # Both classes have a method called sound().

# Object creation
d = Dog()
d.sound()
print("\n")

# super also use with constructor 

# Parent Class
class Person:
    def __init__(self, name):
        self.name = name                   # Parent constructor called

# Child Class
class Student(Person):
    def __init__(self, name,course):
        super().__init__(name)             # calling parent constructor
        self.course = course               # Child constructor called

# Object creation
s1 = Student("Rahul","IT")

print("Name:", s1.name)
print("Course:", s1.course)
