
# what is in backpack game

import random
import os

players = [ {'name':'',
             'score':0,
             'backpack':[]
             },
            {'name':'',
             'score':0,
             'backpack':[]
             }
            ]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Welcome to what is in backpack game')

# setup the players information

for i in range(2):
    players[i]['name']=input('please name the No.{0} player>>>'.format(i+1))
    print('please input 4 items for {0}'.format(players[i]['name']))
    for j in range(4):
        players[i]['backpack'].append(input('please put the No.{0} item to backpack>>>'
                                            .format(j+1)))
    clear_screen()

game_on = True
round = 0

while game_on:
    round += 1
    for i in range(2):
        this_player = players[i]
        other_player = players[(i+1)%2]
        print ("{0}'s turn to guess the backpack of {1}"
               .format(this_player['name'],other_player['name']))
        player_guess = input('>>>>>>')
        if player_guess in other_player['backpack']:
            this_player['score'] += 1
            print("you successfully guessed one item from {0}'s backpack"
                  .format(other_player['name']))
            other_player['backpack'].remove(player_guess)
        else:
            print('You did not get it!')
        print ('Next player')

    print('{0} round ended!'.format(round))
    if (len(other_player['backpack']) == 0) or (len(this_player['backpack']) == 0):
        game_on = False
        break
    play_again = input('want continue next round?(no to end)')
    play_again = play_again.lower()
    if play_again == 'no' or play_again == 'n':
        game_on = False

print('Game End!')
for i in range(2):
    print("player {0} finished with score {1}"
          .format(players[i]['name'],players[i]['score']))
    if len(players[i]['backpack'])>0 :
        print('The backpack have left with: {0}'.format(str(players[i]['backpack'])))

                       
