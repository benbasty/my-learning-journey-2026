# Type Your name Ben.
# Entering something else than your name
# will prompt you to type your name until it is typed right

# this line creates an infinite loop,
# a while loop which condition is always true
while True:
    print('Hi Ben. Please Type Your Name.')
    name = input('> ')
    if name == 'Ben' or name == 'ben':
        break
print('Thank You')