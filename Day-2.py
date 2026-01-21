#  TYPES OF OPERATOR
a=50
b=20

#  1.ARITHMETIC OPERATOR
print(a+b)         #ADDITION
print(a-b)         #SUBSTRACTION
print(a*b)         #MULTIPLICATION
print(a/b)         #DIVISION
print(a%b)         #MODULE
print(a**b)        #POWER

#  2.RELATIONAL OPERATOR
print(a==b)        #EQUAL TO
print(a!=b)        #NOT EQUAL TO
print(a>=b)        #GREATER THAN EQUAL TO
print(a<=b)        #lESS THAN EQUAL TO 
print(a<b)         #LESS THAN
print(a>b)         #GREATER  THAN 

#  3.ASSIGNMENT OPERATOR
num=20
NUM=num+10
print(NUM)

#OR used to add to current valur
num=+20                 #or num+=20
num*=20
num-=20
num/=20
num*=20
num%=20
num**=20

#  4.LOGICAL OPERATOR
print(not True)         #False
print(not False)        #True
print(a>b)              #True
print(a<b)              #False
print(a>b and a>b)      #True
print(a>b and a<b)      #False
print(a>b and a>b)      #True
print(a<b and a<b)      #False

"""
       TYPES OF CONVERSION
       CONVERSION (automatically)
       CASTING (forcefully manually)
"""
a=2              #int
b=4.5            #float
sum=a+b          #python convert int to float becz float is superior
print(sum)       #this is automatic conversion

a="2"            #string
b=4.5            #float
                 #python can not convert string to float or can not add
                 
a=int("2")       #but we can do it forcefully i.e casting
sum=a+b
print(sum)
print(type(sum))

a=3.14
a=str(a)
print(type(a))

#  TAKING INPUT
Name=input("enter yur name: ")
print("welcome", Name)
print(type(Name))

Age=input("enter your age: ")

Phone=input("enter your phone no: ")
print(type(Phone))

