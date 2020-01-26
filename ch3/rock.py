
import random

winner = ''

random_choice = random.randint(0, 2)

computer_choice = ''
user_choice = ''

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'scissors'
elif random_choice == 2:
    computer_choice = 'paper'
else:
    computer_choice = 'none'

""" loop agin when user_choice not rock, scissor or paper """
while ( user_choice != 'rock' and
        user_choice != 'scissors' and
        user_choice != 'paper'):
    user_choice = input('rock, paper and scissors? ')

if computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'computer'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'computer'
elif computer_choice == user_choice:
    winner = 'Tie'
else:
    winner = 'You'

if winner == 'Tie':
    print('We both chose', computer_choice + ', play agin.')
else:
    print(winner, 'won. The computer choice', computer_choice + '.')

