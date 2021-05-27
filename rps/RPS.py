import random
play = 'yes'

# Random function picks a random element from the choices list
def computer(choices = ['rock', 'paper', 'scissors']):
    return random.choice(choices)

# The scores are printed as well as the outcome of the game
def score():
    print("\nAll rounds are played. Results:")
    print("You've won",win,"round(s),",draw,"round(s) resulted in a draw and you've lost",lose,"round(s)!")
    if win > lose:
        print("\nCongratulations! You've won the game!")
    elif win == lose:
        print("\nIt's a draw... I'll beat you next time!")
    else:
        print("\nToo bad, you've lost... Better luck next time")

# Message for wrong input
def notpossible():
    print("\nYou can only enter rock, paper or scissors (You can also type r, p or s).")
    print("Please try again...")

# Determines who wins the round
def round():
    if x == player:
            print("\nYou've picked the same as the computer, it's a draw.")
            result = 'draw'
    elif x == 'rock':
        if player == 'paper':
            print("\nYou've won this round. Paper beats Rock!")
            result = 'win'
        elif player == 'scissors':
            print("\nToo bad, Rock beats Scissors, you've lost this round.")
            result = 'lose'
        else:
            result = 'notpossible'
    elif x == 'paper':
        if player == 'rock':
            print("\nToo bad, Paper beats Rock, you've lost this round.")
            result = 'lose'
        elif player == 'scissors':
            print("\nYou've won this round, Scissors beats Paper!")
            result = 'win'
        else:
            result = 'notpossible'
    elif x == 'scissors':
        if player == 'rock':
            print("\nYou've won this round, Rock beats Scissors!")
            result = 'win'
        elif player == 'paper':
            print("\nToo bad, Scissors beats Paper, you've lost this round.")
            result = 'lose'
        else:
            result = 'notpossible'
    return result

# Function to start a new game
def newgame(yesorno = ['yes', 'no']):
    play = input("\nDo you want to play another game? yes or no? ")
    while play not in yesorno:
        print("Please type yes or no")
        play = input("\nDo you want to play another game? yes or no? ")
    if play == 'yes':
        print("Great! Prepare to lose!")
    return play

print("\nWelcome to Rock Paper Scissors! Can you beat me?\n")

while play == 'yes':

    win = 0
    lose = 0
    draw = 0
    counter = 0

    try:
        rounds = int(input("Please enter how many rounds you want this game to last: "))
    except ValueError:
        print("Please enter a number")
        continue

    print("\nAlright!",rounds,"round(s)! Let's go!")

    while counter < rounds:
        print("\nRound",counter + 1)
        player = input("What do you pick? type rock, paper or scissors (You can also type r, p or s): ")
        if player == 'r':
            player = 'rock'
        elif player == 'p':
            player = 'paper'
        elif player == 's':
            player = 'scissors'
        x = computer()
        result = round()
        if result == 'win':
            win += 1
            counter += 1
        elif result == 'lose':
            lose += 1
            counter += 1
        elif result == 'draw':
            draw += 1
            counter += 1
        else:
            notpossible()
            
    score()
    play = newgame()

print("\nThank you for playing, hope to see you again soon!\n")