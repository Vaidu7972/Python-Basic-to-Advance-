#  FOR LOOP
#  used for sequential traversal of list, tuple, string or any other iterable object

num=[1,2,3,4,5,6,7,8,9,10]
for i in num:                   #in keyword is used to traverse the elements of iterable object
    print(i)
    
name="Vaidehi"
for i in name:
    print(i)    
else:
    print("Loop is ended")
    
name="Vaidehi"
for i in name:
    if i == 'z':
        print("V Found")    
    else:
        print("no")    
    
#  EXAMPLES 
       
""" Print elements of list using loop 
[1,4,9,16,25,36,49,64,81,100] """

a = [1,4,9,16,25,36,49,64,81,100]
for element in a:
    print(element)
    
#  Search no X in tuple using loop
a = [1,4,9,16,25,36,49,64,81,100]
x = 25
for i in range(len(a)):                       #index starts from 0
    if a[i] == x:
        print("Element Found at index:",i)
        break
    
#RANGE FUNCTION

"""range(start, stop, step)

1. start: starting value of the sequence (inclusive). Default is 0. optional value
2. stop:  ending value of the sequence (exclusive).
3. step:  difference between each pair of consecutive values in the sequence. Default is 1.

Returns a sequence of numbers,increase by 1 by default,star from  0 and stops before a specified number."""

for i in range(5):          #0 to 4
    print(i)

#or

a=range
for i in range(5):           #range(stop)
    print(i)

for i in range(1,11):      #1 to 10         range(start,stop)
    print(i)

for i in range(1,11,2):    #1 to 10 with step 2
    print(i)

for i in range(10,0,-1):   #10 to 1 with step -1   range(start,stop,step)
    print(i)

#  PASS STATEMENT (SKIP)

"""IT IS A NULL STATEMENT THAT DOES NOTHING.
IT IS USED AS PLACEHOLDER FOR FUTURE CODE. """

for i in range(5):
    pass                       # here above like/loop does nothing i.e not print anything
print("Hello Vaidehi")  

#  EXAMPLLES

#  QUE : find the sum of n natural numbers

#  WHILE LOOP

n = 10
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1

#  USING RANGE FUNCTION

n = 10
sum = 0
for i in range(1, n + 1):
    sum = sum + i

# Que: factorial of a no 

#using for

n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial of", n, "is", fact)

#using while

n = 5
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("Factorial of", n, "is", fact)







