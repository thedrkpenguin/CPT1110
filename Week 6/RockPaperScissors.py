from random import randint

COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3
#LIZARD =
#SPOCK =

def main():
    result = TIE
    while result == TIE:
    
        computer = randint(1, 3)
        player = int(input('Enter 1 for rock, ' \
                           '2 for paper, 3 for scissors: '))

        print ('Computer chose', choiceString(computer))
        print ('You chose', choiceString(player))
        
        result = rockPaperScissors(computer, player)
        
        if result == TIE:
            print('You made the same choice as ' \
                  'the computer. Starting over')

    if (result == COMPUTER_WINS):
        print ('The computer wins the game')
    elif result == PLAYER_WINS:
        print ('You win the game')
    else:
        print ('You made an invalid choice. No winner')

def rockPaperScissors(computer, player):
        
    if(computer == player):
        return TIE
    
    if computer == ROCK: 
        if player == PAPER: 
            return PLAYER_WINS
        elif player == SCISSORS: 
            return COMPUTER_WINS
        else:
            return INVALID
    elif computer == PAPER: 
        if player == ROCK: 
            return COMPUTER_WINS
        elif player == SCISSORS: 
            return PLAYER_WINS
        else:
            return INVALID
    else: 
        if player == ROCK: 
            return PLAYER_WINS
        elif player == PAPER: 
            return COMPUTER_WINS
        else:
            return INVALID
            
def choiceString(choice):
    if choice == ROCK:
        return 'rock'
    elif choice == PAPER:
        return 'paper'
    elif choice == SCISSORS:
        return 'scissors'
    else:
        return 'something went wrong'

if __name__ == '__main__':
    main()


