# FILE I/O
"""
python can be used to perform operations on files (read and write data).
  
types of files:
1. text files   = human readable files   (.txt,.doc,.log,.csv,.json,.xml etc)
2. binary files = machine readable files (.exe,.bin,.dat,.jpg,.png,.mp3 etc)
3. database files = structured data files (.db,.sql,.mdb etc)

f = open("file_name", "mode")   # open a file and return a file object

FILE MODES:
'r'  = read mode (default mode, file must exist)
'w'  = write mode (overwrite existing file,if file not exist then creates new file)
'a'  = append mode ( appends to write at the  end of the file)

'x'  = create new file mode (creates new file, error if file exists)

't' = text mode (for text files, default mode)
'b' = binary mode (for binary files)

'r+' = read and write mode (file must exist)
'w+'= write and read mode (creates new file or overwrites existing file


FILE OPERATIONS:
1. open()    = to open a file before reading/writing
2. read()    = to read data from a file
3. write()   = to write data to a file
4. close()   = to close a file
5. with statement = to automatically close a file after operations


MEMORY TYPES:
RAM : volatile memory (temporary storage)
HDD/SSD : non-volatile memory (permanent storage)


here first create "D1.txt" file with some text data before running this code.
"""
#open a  file and read data

file=open("D1.txt", "r")   # open file in read mode, this is default mode
                           #here we only give file  name becz another file  in same folder if we give path then it will search for file in that path
data=file.read()           #read data from file and store in variable
print(data)                #print data
file.close()               #close the file
                           #it is necessary to close the file after operations
                        
f=open("D1.txt","r")
print(f.read(6))           #read first 6 characters 
f.close()

f=open("D1.txt","r")
line1=f.readline()          #read and print first line
print(line1)

line2=f.readline()          #read and print second line

print(line2)
f.close()

# Open a file and write data(overwrite mode)

file=open("D1.txt","w")                                             #open file in write mode, this is overwrite mode
                                                                    #if file not exist then it creates new file
file.write("first two lines will replace / over write here.\n\n")   #write data to file
file.close()         

#here overwrite means in file we wrote two line which is replaced by this single line
#if file not exist then it creates new file e.g D2.txt not created
f=open("D2.txt","w")
f.write("This is a new file D2.txt created using write mode.\n")
f.close()

# Open a file and append data (write at the end of the file)

file=open("D1.txt","a")                                   #open file in append mode  
                                                          #if file not exist then it creates new file
file.write("This line is appended to the file.\n\n")      #append data to file
file.close()                                              #close the file after operations

# r+ read and write mode (file must exist)

f=open("D1.txt","r+")                           #open file in read and write mode,file must exit.                                                                    
f.write("This line is written in r+ mode.\n")   #write data to file in r+ mode
data=f.read()                                   #read data from file
                                                # data is written at start of the file.

#w+ write and read mode (creates new file or overwrites existing file)

f=open("D1.txt","w+")                           #open file in write and read mode
                                                 #if file not exist then it creates new file             
f.write("w+ overwite.\n")                       #write data to file
data=f.read()                                   #read data from file
                                                # data is written at start of the file.                                 
f.close()                                       #close the file after operations

#a+ append and read mode (creates new file or appends to existing file)

f=open("D1.txt","a+")                           #open file in append and read mode
                                                #if file not exist then it creates new file                                         
f.write("This line is written in a+ mode.\n")   #append data to file
data=f.read()                                   #read data from file
                                                # data is appended at end of the file.
f.close()                                       #close the file after operations