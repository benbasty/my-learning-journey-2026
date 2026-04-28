username = 'ben'
password = 'weird'
print('Enter your username:')
username_input = input('> ')
print('Enter your password:')
password_input = input('> ')
if username == username_input:
    print(f"Hello {username.capitalize()}!")
    if password == password_input:
        print('Access granted')
    else:
        print('Wrong Password, Please Try Again!')
else:
    print('Wrong Username. Please Try Again!')