print('What\'s your name?')
name = input('> ')
print('What\'s your age?')
age = input('> ')
print(f"Hi {name.capitalize()}!")
if int(age) < 12:
    print('You shouldn\'t be here kiddo')
elif int(age) > 2000:
    print('Ooops there\'s an immortal vampire here.')
elif int(age) > 100:
    print('You are super old but nice to see u here!')
else:
    print('Welcome Back!')