# Types of files:
# 1. Text files: .txt, .docx, .log etc
# 2. Binary files: .jpeg, .png, .mov, .mp4

# fie open -> read -> close
file = open("demo.txt", "r")
# data = file.read() # reads the whole file
# print(data)
# data = file.read(5) # reads first 5 letters
# print(data)
line1 = file.readline() # reads first line
print(line1) 
line2 = file.readline() # reads second line
print(line2) 
file.close()

# character ------------ meaning
# r         ------------ open for reading (default)
# w         ------------ open for writing, truncating the file first
# x         ------------ create a new file and open it for writing
# a         ------------ open for writing, appending to the end of the file if it exists
# b         ------------ binary mode
# t         ------------ text mode (default)
# +         ------------ open a disc file for updating (reading and writing)
# r+        ------------ read + overwrite (pointer at the start), without truncating
# w+        ------------ read + overwrite, truncates
# a+        ------------ read + append (pointer at the end), without truncating

# file open -> append -> close -> file open -> read -> close
file3 = open("demo.txt", "a")
file3.write("\nappending a new line")
file3.close()
file3 = open("demo.txt", "r")
append_data = file3.read() 
print(append_data)


# file open -> write -> close -> file open -> read -> close
file2 = open("demo.txt", "w")
file2.write("Deleted previous text and added this new text.")
file2.close()
file2 = open("demo.txt", "r")
new_data = file2.read() 
print(new_data)


# with syntax for file in python
# when with syntax is used, file closes automatically, don't need to close file explicitly
with open("demo.txt", "r") as file: # means open the file demo.txt as a stream named 'file'
    with_syntax_file_data = file.read()
    print(with_syntax_file_data)
    
# deleting a file
# have to use os module for it
# module(like a code library) is a file written by another programmer that generally has functions we can use
# import os
# os.remove("demo.txt")