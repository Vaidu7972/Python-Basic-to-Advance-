 # FUNCTIONS 

"""Block / Group of code that performs a specific task.
reusable code.
avoid rewriting the same code again and again.(reduce code redundancy)
(DRY- Don't Repeat Yourself)

Two types of functions:   

1. Built-in functions: 
   pre-defined functions in python
   e.g.- print(), input(), len(), type(), range(), int(), str() etc

2. User-defined functions: 
   functions defined by the user to perform specific tasks.
  

Syntax:
def function_name(parameters / inputs):
keyword 'def' is used to define a function.
"""

a=10
b=20
c=a+b
print("Sum is:",c)
print(c,"\n")

#instead of writing above code again and again we can use function

def add_numbers(x, y):             #function definition  #a,b are parameters 
    c = x + y
    print(c,"\n")
    
add_numbers(10,20)                    #function call  #10,20 are arguments
add_numbers(100,200)                  #function call  

#or

def add_numbers(x, y):
    return x + y                      #fuction definition 

result = add_numbers(10, 20)         #function call
print(result,"\n")


#  1. Fuction with arguments and return Type 

def square(num):                    #fuction call
    return num * num                #function definition

result = square(5)
print(result,"\n")

#  2. function with no arguments and no return type

def greet():
    print("Hello, Welcome to Python Functions!\n")

greet()                             #function call
greet()                             #function call

#  3. function with arguments and no return type

def greet(name):
    print("Hello", name, "Welcome to Python Functions!\n")  

greet("vaidehi")                     #function call

# 4. function with no arguments and return type

def greeting():
    return "Hello, Welcome to Python Functions!\n"

message = greeting()                 #function call
print(message)

# EXAMPLE : avg of 3 numbers

def average(a,b,c):          #this is not return type function
    avg = (a+b+c)/3
    print(avg)
    return avg
    
    average(10,20,30)       #function call
    
def cal_average(a,b,c):     
    sum = a + b + c
    avg = sum / 3
    print("Average is:", avg)   
    return avg
average(1,2,3)   
    
#  by default arguments    

def power(a,b=2):
    result = a ** b
    print(result)

power(5)                             # here b takes default value 2
power(2,3)                           # here b takes value 3,overrides on default value
