#  LIST
"""
    - Builn datatype (stores int, str, float  etc)
    - Mutable can be change.
    - List can acceess as well as change.
    - Index start from zero
"""
marks=11
marks=22
marks=33
marks=44    
marks=55

#  instead of this  we  can write list at a time as follows--->

marks=[11,22,33,44,55]
print(marks)             
print(type(marks))        #data-type of list
print(len(marks))         #length of list
print(marks[0])           #prints 1st number

#  Replace in List

stu=["Vaidehi", 20, "IT"]
print(stu)
stu[0]="Vaidu"
print(stu)

#or

stu.insert(1,"VV")                   # use to add at index 1 new element
print(stu)

#  LIST SLICING
"""
    - similar to string slicing
    - slicing  is subsett of list
"""
print(marks[:2])              #prints start to number before 2 (not 2)
print(marks[1:])              #print from 1 (including 1) to end  
print(marks[1:3])             #print  from  1  to  number before 2 (not 3)
print(marks[-3:-1])

#i.e before : print bt not after : not print

#  LIST METHOD :

list=[2,1,3,5,4]

print(list.append(6))         # append() : adding in list
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list=[2,1,3,5,4]
list.reverse()
print(list)

list.insert(1,9)
print(list)

list.insert(5,9)
print(list)

list.remove(5)
print(list)

list.pop(1)
print(list)


