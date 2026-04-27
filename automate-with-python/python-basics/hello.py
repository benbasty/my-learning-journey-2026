# This program says Hello and ask for your name and age
print('Hello World!')
print('What\'s your name?')
name = input('> ')
name = name.capitalize()
print('It is good to meet you, ' + name)
print('What is your age?') #asks for your age
age = input('> ')
print('You will be ' + str(int(age) + 5) + ' in 5 years.')
print('Thank you for getting to know each others. Till next time.')