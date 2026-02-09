# Different syntax of file I/O
# Open a file in read mode

with open("D2.txt", "w") as file: #open file in write mode, this is overwrite mode
    file.write("This is a new file D2.txt created using write mode.\n")   #write data to file   
    
# no need to explicitly close the file, it will be closed automatically

#r
with open("D2.txt","r") as file:     #open file in read mode using with statement
    data=file.read()                 #read data from file
    print(data)                      #print the data

# no need to explicitly close the file, it will be closed automatically


#a
with open("D2.txt","a") as file:                        #open file in append mode using with statement
    file.write("This line is added in append mode.\n")  #append data to file

# no need to explicitly close the file, it will be closed automatically

# delete
#using OS module to delete a file os stand for operating system
import os
if os.path.exists("D2.txt"):                           #check if file exists
   os.remove("D2.txt")                                 #delete the file

with open ("new.txt","w") as f:                        #open new file in write mode using with statement
    f.write("created  new file write mode.\n")         #write data to file

# no need to explicitly close the file, it will be closed automatically

#EXAMPLES 

#create a new file practice.txt using python and add data 
""" hi everyone
    welcome"""

with open("practice.txt","w") as file:
    file.write("hi everyone\nwelcome")   #write data to file
    
#write a fuction replace in above file hi to hello

with open("practice.txt","r") as file:     #open file in read mode
    data=file.read()      #read data from file
    
    new_data=data.replace("hi","hello")       #replace hi with hello in data    
    print(new_data)
    
with open("practice.txt","w") as file:     #open file in write mode
    file.write(new_data)     #write new data to file
    
#check hello is exit in file
word="hello"
with open("practice.txt","r") as f:
     data = f.read()
     if(data.find(word)!=-1):
          print("found")
     else:
          print("not found")
          