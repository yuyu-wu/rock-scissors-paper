# print('rock')
# import random
from random import randint
# player1 = input('Player 1, make your move: ')
# print('****NO CHEATING!\n\n' * 20)
# player2 = input('Player 2, make your move: ')
player = input('Make your move: ').lower()

# rand_num = random.randint(0,2)
rand_num = randint(0,2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'scissors'
else: 
    computer = 'paper'
print(f'Computer playes {computer}')
# if player1 == 'rock' and player2 == 'scissors':
#     print('Player1 wins!')
# elif player1 == 'rock' and player2 == 'paper':
#     print('Player2 wins!')
# elif player1 == 'scissors' and player2 == 'rock':
#     print('Player2 wins!')
# elif player1 == 'scissors' and player2 == 'paper':
#     print('Player1 wins!')
# elif player1 == 'paper' and player2 == 'rock': 
#     print('Player1 wins!')
# elif player1 == 'paper' and player2 == 'scissors': 
#     print('Player2 wins!')
# elif player1 == player2:
#     print('It\'s a tie!')
# else: 
#     print('Something went wrong!')

# if player1 == player2:
#     print('It\'s a tie!')
# elif player1 == 'rock':
#     if player2 == 'scissors':
#         print('Player1 wins!')
#     elif player2 == 'paper':
#         print('Player2 wins!')
# elif player1 == 'scissors':
#     if player2 == 'rock':
#         print('Player2 wins!')
#     elif player2 == 'paper':
#         print('Player1 wins!')
# elif player1 == 'paper':
#     if player2 == 'rock':
#         print('Player1 wins!')
#     elif player2 == 'scissors':
#         print('Player2 wins!')
# else: 
#     print('Something went wrong!')

if player == computer:
    print('It\'s a tie!')
elif player == 'rock':
    if computer == 'scissors':
        print('You win!')
    else:
        print('Computer wins!')
elif player == 'scissors':
    if computer == 'rock':
        print('Computer wins!')
    else:
        print('You win!')
elif player == 'paper':
    if computer == 'rock':
        print('You win!')
    else:
        print('Computer wins!')
else: 
    print('Please enter a valid move!')