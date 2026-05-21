#import Path
# The Path() function in the pathlib module handles all operating systems
from pathlib import Path
# accessing the home directory
# print(Path.home())
# creating new folders
# import os
# os.makedirs('automating-tasks')
import time

# The File Reading and Writing Process
#write text and read text

p = Path('hello.txt')
# write_text() method creates a new text file (or overwrites an existing one)
p.write_text('Hello, Nice to meet u')
print(p.read_text())
# The pathlib module’s read_text() method returns the full contents
# of a text file as a string.

#get current working directory
# print(Path.cwd())

# Creating New Folders
# w = 'waffles'
# os.makedirs(w)
# create the waffles folder inside the current directory

# Finding File Sizes and Timestamps
# The stat() method returns a stat_result object with file size
# and timestamp information about a file.
file = Path('/Users/benbasty/Downloads/my-learning-journey-2026/automate-with-python/python-basics/hello.txt')
print(file.stat().st_size)
print(file.stat().st_mtime)
print(time.asctime(time.localtime(file.stat().st_mtime)))

#The File Reading and Writing Process

# Opening Files
# To open a file with the open() function, pass it a string path indicating the file 
# you want to open. This can be either an absolute path or a relative path. 
# The open() function returns a File object.

hello_file = open(Path.cwd() / 'hello.txt', encoding='UTF-8')
print(hello_file)
print(hello_file.read())

# Writing to Files
# check up

# Using with Statements