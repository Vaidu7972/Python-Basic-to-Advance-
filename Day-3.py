#  String
print('Vaidehi')
print("Vaidehi")
print("""Vaidehi""")
print('Vaidehi is a girl')
print(" ")

#  NEXT LINE
print("This is \n Next line")  #not this (/)
print("\n")

#  CONCATINATION (JOIN CHAR)

str1="sun"
str2="light"
print(str1 +" "+  str2)          #we can add more than two 
print("sun"+"shine")


#  Length

a="Vaidehi "                     #Space also considers
print(len(a))

#  INDEXING (start with zero. use for access char, cannot  modify)

print(a[0])
print(a[1])

#  SLICING  (access part  of string)  (start with 0)

#forward
str="Doing Slicing"
print(str[6:13])              #only prints part mentioned with index 6 to 13
print(str[:])                 #print all
print(str[0:])                #prints all without end
print(str[:13])               #prints all without start

#backend (negative indexing)
print(str[-7:-1])             #start with -1 (i.e -5 -4 -3 -2 -1)

# STRING FUNCTION (There are too many functions of string but following are main

x="i am a coder"

print(x.endswith("er"))
print(x.capitalize())
print(x.replace("coder","Vaidehi"))
print(x.find("i"))
print(x.count("a"))