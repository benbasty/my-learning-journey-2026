birthdays = {'Alice': 'Apr1', 'Anna': 'Dec1', 'Alex': 'May 23'}
while True:
    print('Enter a name: (blank to quit)')
    name = input('> ')
    if name == '':
        break
    if name in birthdays:
        print(name + '\'s birthday is ' + birthdays[name])
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input('> ')
        birthdays[name] = bday
        print('Birthday database updated.')