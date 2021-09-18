# ghost game

import random

score = 0

print('Welcome to Ghost Game')

ghost = random.randint(1,3)

go_ahead = True

while go_ahead:
    print('There are 3 doors in front of you.')
    print('One of the door if you open you will see a GHOST!')

    door = input('Choose which door you want to open, 1, 2, or 3?>>>')

    if door.isdigit():
        door = int(door)
        if door == ghost:
            print('GHOST!!! run away!')
            go_ahead = False
        elif door<1  or door >3:
            print('wrong door number')
            continue
        else:
            print('no ghost')
            score += 1
            continue
    else:
        print('wrong door number')
        continue
    
print('You have passed {0:d} times the ghost door.'.format(score))
print('Game End!')
