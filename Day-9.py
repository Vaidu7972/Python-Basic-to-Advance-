""" 
LOOPS
for loop, while loop
Lops are use to repeat a instruction or block of code multiple times 
"""

# WHILE LOOP

# Infinite Loop
while True:
    print("Hello World","\n")       # This will print Hello World infinitely
    break                           # This will break the infinite loop
print("\n")

#  FINITE LOOP
count = 1
while count <= 5:                   #While condition, Print HEllo world 5 times
    print("Hello World", count)
    count += count+1                # Increment the count by 1