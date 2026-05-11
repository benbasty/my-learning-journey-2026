#import Path
# The Path() function in the pathlib module handles all operating systems
from pathlib import Path
# accessing the home directory
# print(Path.home())
# creating new folders
# import os
# os.makedirs('automating-tasks')

# The File Reading and Writing Process
#write text and read text

p = Path('hello.txt')
p.write_text('Hello, Nice to meet u')
print(p.read_text())
