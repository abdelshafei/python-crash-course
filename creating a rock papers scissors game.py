import random

def get_choices():


    player_choice = input('Enter a choice (rock, paper, scissors): ').lower()
    options = ["rock", "paper", "scissors"]  
    computer_choice = random.choice(options)

    choices = {'player' : player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer):
    print(f'You chose {player}, however the computer chose {computer}')
    if player == computer:
        return 'Its a tie!'
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! You win!'
        elif computer == 'paper':
            return ' Paper catches rock! You lose.'
        else:
            return 'You have to input any of the following words: ("rock", "paper" or "scissors")'    
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper Catches rock! You win!'
        elif computer == 'scissors':
            return 'Scissors cuts paper! You lose.'
        else:
            return 'You have to input any of the following words: ("rock", "paper" or "scissors")'    
    elif player == 'scissors':
        if computer == 'rock':
            return 'Rock smashes scissors! You lose.'
        elif computer == 'paper':
            return 'Scissors cuts paper! You win!'
        else:
            return 'You have to input any of the following words: ("rock", "paper" or "scissors")'                      
    else:
        return 'You have to input any of the following words: ("rock", "paper" or "scissors")'

respones = get_choices()

result = check_win(respones['player'], respones['computer'])

print(result)