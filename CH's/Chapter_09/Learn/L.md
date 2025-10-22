```python
'''
f = open("hi.txt")
print(f.read())
f.close()
'''

'''
f=open("myfile.txt","w")
f.write("Hi This Is MyFile.txt File Created By Python")
f.close()
print("File Created Successfully")
# print(f.read())  # This will not work as the file is opened in write mode
f=open("myfile.txt","r")
print(f.read())
f.close()
'''
'''
line=open("Learn/myfile.txt","r")
print(line.read())  # Reading the entire file
print(line.readline())  # this will not work as the file pointer is at the end after read()
line.close()


line=open("Learn/myfile.txt","r")  
print(line.readline()) # Reading the first line
print(line.readline()) # Reading the second line
print(line.readline()) # Reading the third line
print(line.readline()) # Reading the fourth line
print(line.readline()) # Reading the fifth line
print(line.readline()) # Reading the sixth line
print(line.readline()) # Reading the seventh line       
line.close()

line=open("Learn/myfile.txt","r")
print(line.readline())  # Reading all lines as a list
print(line.read())  # This wiill read the rest of the file
line.close()    
'''

'''
line=open("Learn/myfile.txt","r")
print(line.readlines())  # Reading all lines as a list
print(line.read())  # This will read the rest of the file, which is empty now
line.close()
'''
'''
line=open("Learn/myfile.txt","r")
print(line.read())
print(line.readlines())  # This will return an empty list as the file pointer is at the end
line.close()
'''
'''
with open("Learn/myfile.txt", "r") as line:    #this will open the file and automatically close it after the block
    print(line.read())  # Reading the entire file
    print(line.readline())  # This will not work as the file pointer is at the end after read()
'''

```