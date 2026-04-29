print ("HEllO")        #string is written in double quotes
print(23)          
print("Vpf","errr")

print("Hello")                   #double  ("")  (' ') (""" """)  same working 
print('Hello')                   #single
print('''Hello''')               #triple
print("Myself Vaidehi Doke ")    #sentence
print(20)                        #number

#  COMMENT
  
# used for comment
# python is case - Sensitive 
# a=2 A=2 different both 

"""
    THIS
    IS
    MULTILINE  
    COMMENT
"""

#  VARIABLES & INDENTIFIER

name = "vaidehi"   #here name is variable 
age = 23
price = 25.99
print(type(name))                                              
print ("my name is ", name)                 
print (" my age is", age)                               
price2=print((price*2))

"""
Rules:             
1. identifier can combination of uppercase & lowercase , digits or underscore myvar1 , my_var
2. identifier cannot start with digit 
3. we cant use symbol
4. it can be of any length 
"""

#  DATA TYPES (inbuild/buildin & userdefine)
name = "vpd"
age = 23
price = 22.99
old = True
print(type(name))     #str
print(type(age))      #int
print(type(price))    #float 
print(type(old))      #boolean 
a=None                #none type
print(type(a))
b=1j                  #complex
print(type(b))

x=["apple","banana","cherry"]   #list mutable can change
y=("apple","banana","cherry")   #tuple
z={"apple","banana","cherry"}   #set
print(type(x))
print(type(y))
print(type(z))

#  APPEND (used to add single element after the list  )

x.append("abc")
print(x)           #['apple','banana','cherry','abc']

#  CASTING

a=float(2)
b=str(2)

#  CONVERT

c=2
d=3.22
e=2j
f=print(float(c))         # int to float
g=print(int(d))           # float to int
h=print(complex(c))       # float to complex

#  UPPER LOWER

k="Hello"
u=print(k.upper())
o=print(k.lower())

#  SUM & DIFFERENCE

a=3
b=2

c=(a+b)
print(c)

d=(a-b)
print(d)
