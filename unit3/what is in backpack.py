
'''
what is in backpack game
'''

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_intro():
    print('Welcome to what is in backpack game')

def game_init(players):
    # setup the players information
    for i in range(2):
        players[i]['name']=input(f"please name the No.{i+1} player>>>")
        print(f"please input 4 items for {players[i]['name']}")
        for j in range(4):
            players[i]['backpack'].append(input(f"please put the No.{j+1} item to backpack>>>"))
        clear_screen()


def main():
    players = [
        {'name':'',
            'score':0,
            'backpack':[]
        },
        {'name':'',
            'score':0,
            'backpack':[]
        }
    ]
    game_on = True
    round = 0

    game_intro()
    game_init(players)

    while game_on:
        round += 1
        for i in range(2):
            this_player = players[i]
            other_player = players[(i+1)%2]
            print(f"{this_player['name']}'s turn to guess the backpack of {other_player['name']}")
            player_guess = input('>>>>>>')
            if player_guess in other_player['backpack']:
                this_player['score'] += 1
                print(f"you guessed one item from {other_player['name']}'s backpack")
                other_player['backpack'].remove(player_guess)
            else:
                print('You did not get it!')
            print ('Next player')

        print(f'{round} round ended!')
        if (len(other_player['backpack']) == 0) or (len(this_player['backpack']) == 0):
            game_on = False
            break
        play_again = input('want continue next round?(no to end)')
        play_again = play_again.lower()
        if play_again in ('no', 'n'):
            game_on = False

    print('Game End!')
    for i in range(2):
        print(f"player {players[i]['name']} finished with score {players[i]['score']}")
        if len(players[i]['backpack'])>0 :
            print(f"The backpack have left with: {players[i]['backpack']}")

if __name__ == '__main__':
    main()
