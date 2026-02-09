# OOP : Object Oriented Programing
# OOP 4 pillors: Abstraction 
#                Encapsulation
#                Inheritance
#                Polymorphism

"""
POP : procedural orientent programing.  
      Programming is done using functions.
      We focus on what to do step by step.
      Program is divided into functions
      Data is passed from function to function.
      
Functions: redundancy dec and reusability.(def)

OOP : Programming is done using objects and classes. (class & obj with def)
      We focus on real-world things.
      Program is divided into classes and objects.
      Data and functions are together in one place.
      first we create class then object.


Class : it is a blueprint(info) for obj.
        e.g stu(class)
        class stores two things Data (att) & Methods

Object : instace of class.
        e.g name,age,..(obj/info)
        
"""     

#class

class stu:
      name="Vaidehi"
      
#object 
s1 = stu()
print(s1.name)   
   
class Car:                      #creating class
    color = "blue"
    brand = "mercedes"

car1 = Car()                    #creating object
print(car1.color)
print(car1.brand)
   
# Constructor
""""
    __init_() function : it is special funct called constructor
    invoke at the time of obj creation.
    All classes have a function called __init_(), 
    which is always executed when object is being initiated.
    init fuct always executed if we write it or not ther is always constructor
"""
# Default Constructor
def __init_(self):                        #only self/created bydefault
    print("default constructor")
    pass

# Paramerterized Constructor
class student:                           #self:it is a refrence to the current instance of class,allows the object to access its own data and functions.
    def __init__(self,name,age):         #self as well as other parameters (always self parameter/argument take by consructor)
        self.name=name                   #if we not write self then give error so it is compulsory we can give diff name instead of self write any think but mostly use self
        self.age=age
        
s1=student("Vaidehi",21)                   #():use for call constructor,what ever we write in ()will execute
print(s1.name,s1.age)

s2=student ("prateek",12) 
print(s2.name,s2.age,"\n")

#OR

class Student:
    def __init__(self,fullname):      #self parameter is a reference to current instance of class, used to access variables that belongs to class.
        self.name = fullname

s1 = Student("Vaidehi")
print(s1.name)

# Attributes 
"""
 Class Attribute     (common attribute) 
 Instance Attribute  (diff attributes)
 if class and obj having same atributes with diff values then object>> class(override).
"""

class student:    
    college="Trinity"            

    def __init__(self,name,age):        
        self.name=name                   
        self.age=age
        
s1=student("Vaidehi",21)    
print(s1.name,s1.age)   
print(s1.college,"\n")           

# Methods
"""
method is function belong to object
"""
 
#creating class in method
class student:

    def __init__(self, name):             # Constructor
        self.name = name

    def welcome(self):                     # Method   (always self)
        print("Welcome,", self.name)


# Creating object
s1 = student("Vaidehi")
s1.welcome()
print("\n")

#Static Methods
"""
don't use self parameter/argument. (They work at class level)
works at class level.
Decorators: diffetrnt types of decorator.
            allows us to wrap another function in order to extend behaviour of wrap funtion,
            without permrntly modify it.
            This method does not use self
            It belongs to the class, not to an object
"""

class stu:
    @staticmethod              #decorator
    def col():
        print("Trinity")


stu.col()                      # Calling static method