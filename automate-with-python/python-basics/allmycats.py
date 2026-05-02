import random
cat_names = []
while True:
    print('Enter the cat\'s name ' + str(len(cat_names) + 1) + ' or enter nothing to stop:')
    name = input('> ')
    if name == '':
        break
    cat_names = cat_names + [name]
print('The cats names are:')
for name in cat_names:
    print(name)
print('Your favorite cat is ' + random.choice(cat_names))