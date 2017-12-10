"""
1	r:Opens a file for reading only. 
The file pointer is placed at the beginning 
of the file. This is the default mode."""
myFile = open("myFile.txt", "r")
print ("Name of the file: ", myFile.name)
print ("Closed or not : ", myFile.closed)
print ("Opening mode : ", myFile.mode)
print ("Reading the file: ", myFile.read())
#print ("Reading the file: ", myFile.write("Great"))
myFile.close()

"""
2	rb:Opens a file for reading only in binary 
format. The file pointer is placed at the 
beginning of the file. This is the default mode.
"""
myFile = open("myFile.txt", "rb")
print ("Name of the file: ", myFile.name)
print ("Closed or not : ", myFile.closed)
print ("Opening mode : ", myFile.mode)
print ("Reading the file: ", myFile.read())
#print ("Reading the file: ", myFile.write("Great"))
myFile.close()

"""
3	r+:Opens a file for both reading and writing. 
The file pointer placed at the beginning of the file.
"""
myFile = open("myFile.txt", "r+")
print ("Name of the file: ", myFile.name)
print ("Closed or not : ", myFile.closed)
print ("Opening mode : ", myFile.mode)
print ("Reading the file: ", myFile.read())
print ("Reading the file: ", myFile.write("Great"))
myFile.close()
"""
4	rb+:Opens a file for both reading and writing 
in binary format. The file pointer placed at the 
beginning of the file."""

myFile = open("myFile.txt", "r+")
print ("Name of the file: ", myFile.name)
print ("Closed or not : ", myFile.closed)
print ("Opening mode : ", myFile.mode)
print ("Reading the file: ", myFile.read())
print ("Reading the file: ", myFile.write("Great"))
myFile.close()
"""
5	w:Opens a file for writing only. 
Overwrites the file if the file exists. 
If the file does not exist, creates a new file 
for writing

6	wb:Opens a file for writing only in binary format. 
Overwrites the file if the file exists. 
If the file does not exist, creates a new file 
for writing.

7	w+:Opens a file for both writing and reading. 
Overwrites the existing file if the file exists. 
If the file does not exist, creates a new file for 
reading and writing.

8	wb+:Opens a file for both writing and reading 
in binary format. Overwrites the existing file 
if the file exists. If the file does not exist, 
creates a new file for reading and writing.

9	a:Opens a file for appending. 
The file pointer is at the end of the file 
if the file exists. That is, the file is in the 
append mode. If the file does not exist, it 
creates a new file for writing.

10	ab:Opens a file for appending in binary format. 
The file pointer is at the end of the file if the 
file exists. That is, the file is in the append mode. 
If the file does not exist, it creates a new file 
for writing.
11	a+:Opens a file for both appending and reading. 
The file pointer is at the end of the file if the 
file exists. The file opens in the append mode. 
If the file does not exist, it creates a new file 
for reading and writing.
12	ab+:Opens a file for both appending and reading 
in binary format. The file pointer is at the end of 
the file if the file exists. The file opens in the 
append mode. If the file does not exist, it creates
 a new file for reading and writing.
 """
import os
print(dir(os))


myPath = os.path.join("/Users/varmabhupatiraju/Documents/","Docs1")

print(os.listdir(myPath))

os.chdir("/Users/varmabhupatiraju/Documents/Docs1")
print(os.listdir(os.curdir))

#os.rename("divine8.plist","divine.plist")
#os.mkdir("Krish")
print(os.listdir(os.curdir))

#os.rmdir() to remove directory.
#os.rmdir('Krish')
print(os.listdir(os.curdir))

#os.remove() to remove file.
#os.remove("Response.rtf")
f= open('divine8.php','r')
print ("Reading the file: ", f.read())
