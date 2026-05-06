# raw string
print(r'My name is Ben. Nice to meet you')
print(r"Raw strings are helpful if your string values contain many backslashes, such as the strings used for Windows filepaths like C:\Users\Al\Desktop or regular expression strings, which are described in the next chapter.")

print(r'showing hello world indexes')
print('''
H  e   l   l   o  ,     w  o  r  l  d   !
0  1   2   3   4  5  6  7  8  9  10 11  12
-13-12-11 -10 -9 -8 -7 -6 -5 -4  -3 -2  -1
''')

greeting = 'Hello, world!'
print(greeting[12])
print(greeting[-1])
print(greeting[0:5])
print(greeting[:5])
print(greeting[7:12])
print(greeting[7:-1])

#f strings manipulations
name = 'Al'
age = 4000
print(f'My name is {name}. I am {age} years old!')

#useful strings methods
#changing the case
spam = 'Hello World!'
print(spam.upper())
print(spam.lower())

#strings characteristics

print ('''
issupper() returns a Boolean True value if the string has at least one letter
isLower() returns true if all letters are lower case
isUpper() returns true if all letters are upper case
isalpha() returns True if the string consists only of letters and isn\'t blank
isalnum() returns True if the string consists only of letters and numbers (alphanumerics) and isn\'t blank
isdecimal() returns True if the string consists only of numeric characters and isn\'t blank
isspace() returns True if the string consists only of spaces, tabs, and newlines and isn\'t blank
istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
''')

print('The isX() string methods are helpful when you need to validate user input.')

while True:
    print('Pls Enter Your age:')
    age = input('> ')
    if age.isdecimal():
        break
    else:
        print('The age is not a valid number')


#checking the starts or end of a string
# .startswith()
# .endwith()

#joining and splitting strings

# .join()
joined = ' '.join(['My','Name', 'Is', 'Simon'])
print(joined)
# .split()
splitted = 'My Name Is Simon'.split()