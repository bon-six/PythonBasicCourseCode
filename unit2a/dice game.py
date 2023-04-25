

import random

#store the win numbers for player. initial round is 7, 11
win_numbers = [7, 11]

#store the lose numbers for player. initial round is 2, 3, 12
lose_numbers = [2, 3, 12]


def throw_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'you got dice number of {dice1} and {dice2}')
    return dice1+dice2

win = 0
lose = 0

while True:
    print('hit enter key to throw the dices')
    input()
    result = throw_dice()
    if result in win_numbers:
        print('you win!')
        win += 1
        print('Do you want continue play? (yes to continue, no to quit)')
        answer = input()
        if answer.lower() == 'no' or answer.lower() == 'n':
            break
        else:
            win_numbers = [7, 11]
            lose_numbers = [2, 3, 12]
            continue
    elif result in lose_numbers:
        print('you lose!')
        lose += 1
        print('Do you want continue play? (yes to continue, no to quit)')
        answer = input()
        if answer.lower() == 'no' or answer.lower() == 'n':
            break
        else:
            win_numbers = [7, 11]
            lose_numbers = [2, 3, 12]
            continue
    else:
        print('Follow up throw!')
        win_numbers = [result]
        lose_numbers = [7]
print(f'game over.\nyou win {win} times.\nyou lose {lose} times.')
