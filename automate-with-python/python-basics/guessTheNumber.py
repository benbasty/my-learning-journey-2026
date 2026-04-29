# this is a guess number game
import random
secretNumber = random.randint(1,10)
print('I am thinking of a number between 1 and 10')

#ask the player to guess 5 times
for guessesTaken in range(1,6):
    print('Take a guess.')
    guess = int(input('> '))

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # once the guess is correct

if guess == secretNumber:
    print('Great! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinkinng was ' + str(secretNumber))
    print('Welcome to try again')