#@staticmethod doesnt do 
class Person:
    name = "anonymous"               #class attribute
    
    def changeName(self, name):
        self.name = name            #here new attribute creating     #self is object
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)        
print(Person.name)

#if we dont want this will do
class Person:
    name = "anonymous"               #class attribute
    
    def changeName(self, name):
       Person.name = name            #here new attribute creating
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)        
print(Person.name)             #as a result it will print  person class  attributes

#alternative

class Person:
    name = "anonymous"               #class attribute
    
    def changeName(self, name):
        self.__class__.name = "Rahul"         #therefore we can write self.__class__.xyz or Classname.xyz   
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)        
print(Person.name)

""" Class Method
it is bound to class and recives the class as implicit first argument
note: static method can't accesss or modify class state & generally for utility.

class student:
    @classmethod  #decorator
    def college(cls):
    pass
    
    1. Static Method which dont access attributes of class or instance  [class or isntance not touch or use prop]
    2. Class method  which has (cls) as a first implicit argument      [class prop and attributes used ]
    3. Instance Method which has (self) argument                       [instance prop and attributes used]
    """


class Person:
    name = "anonymous"               #class attribute
    
    @classmethod
    def changeName(cls, name):
        cls.name = name            
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)        
print(Person.name)


class Student:
    def __init__(self, phy, chem, math):       
        self.phy = phy                        #values
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        
stu1 = Student(98, 97, 99)
print(stu1.percentage)        
        #percentage attribute