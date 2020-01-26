
color = 'blue'
guess = ''
guesses = 0

while color != guess:

    guess = input('What color am I thinking of? ')

    if color != guess:
        guesses = guesses + 1

print('You got it! It took you', guess, guesses)
