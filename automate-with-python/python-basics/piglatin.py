print('''
########################################################################
Pig latin is a silly made-up language that alters English words.
If a word begins with a vowel, the word yay is added to the end of it.
If a word begins with a consonant or consonant cluster (like ch or gr),
that consonant or consonant cluster is moved to the end of the word
and followed by ay.
########################################################################''')
print('Pls Enter the English message to translate into pig latin:')
message = input('> ')
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pig_latin = [] # A list of the words in pig latin

# get a list of the words as separate strings.
# message.split returns ['My', 'name', 'is', 'AL', 'SWEIGART', 'and', 'I', 'am', '4,000', 'years', 'old.'].
for word in message.split():
    # Separate the non-letters at the start of this word:
    # remove any non-letters from the start and end of each word
    # so that strings like 'old.' translate to 'oldyay.' instead of 'old.yay'
    # We save these non-letters to a variable named prefix_non_letters.
    prefix_non_letters = ''

    # This loop continues as long as the string isn't empty and the first character is not a letter
    # .isalpha() returns True if the character is a letter, and False otherwise.
    while len(word) > 0 and not word[0].isalpha():
        # It takes that non-letter character and saves it into prefix_non_letters
        prefix_non_letters += word[0]
        # It "slices" the string, removing that first character so the loop can check the next one.
        word = word[1:]
    # After the loop finishes, this checks if there is anything left of the word.
    if len(word) == 0:
        # If the word was only non-letters, it adds those symbols to the results list
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of this word:
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]

    # Remember if the word was in uppercase or title case:
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower() # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the word:
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join all the words back together into a single string:
print(' '.join(pig_latin))