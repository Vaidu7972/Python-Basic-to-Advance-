#  Recursive Fuction
"""
When a function calls itself repeatedly.
similar to loops but uses function calls instead of iterative constructs.
loops are generally more efficient in terms of memory and performance.
loops and recursion are interconected.
 i.e, a work done by loop can also be done by recursion and vice versa.
"""

def show(n):                #print n
    if n == 6:              #base case / STOP condition
        return
    print(n)
    show(n+1)              #output will be 1 to 5 and then stop when n becomes 6
    
show(1)
    
    
def show(n):
    print(n)
    
show(5)     

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    
show(5)    

#  Factorial of a number using recursion

def factorial(n):
    if n==0 or n==1:                  # base case / STOP condition
        return 1
    else:
        return n * factorial(n-1)     # recusive case
    
result = factorial(4)
print("Factorial is:", result)        #output: Factorial of 6 is: 720
print("----") 


# or

def factorial(n):
    if n==0:                          # base case / STOP condition
        return 1
    return n * factorial(n-1)     # recusive case
result = factorial(5)
print("Factorial is:", result)        #output: Factorial of 5 is: 120
print("----")   

# EXAMPLES:
# Sum of first n natural numbers using recursion

def sum_n(n):
        if n==1:
            return 1
        return n + sum_n(n-1)
result = sum_n(5)
print("Sum of first 5 natural numbers is:", result)    #output: Sum of first 5 natural numbers is: 15
print("----")

#print all elements in a list hint: use list and index as parameters    

def print_list_elements(lst, index):
    if index == len(lst):          #base case / STOP condition
        return
    print(lst[index])
    print_list_elements(lst, index + 1)   #recursive case   
    
my_list = [10, 20, 30, 40, 50]
print_list_elements(my_list, 0)
print("----")

# Fibonacci series using recursion
#0 1  1 2 3 5 8 13 21 34 .....

def fibonacci(n):
    if n <= 0:                      #base case / STOP condition
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)   #recursive case
    
result = fibonacci(10)
print("Fibonacci number is:", result)    #output: 10th Fibonacci number is: 55
print("----")