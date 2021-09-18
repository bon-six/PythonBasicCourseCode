
import random

# throw the dice and get the sum.
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
result = dice1+dice2

# if it is 7, 11, win the game.
if result == 7 or result == 11:
    print(f'You win. dice1 is {dice1}, dice2 is {dice2}')

# if it is 2, 3, 12, lose
elif result == 2 or result == 3 or result == 12:
    print(f'You lose. dice1 is {dice1}, dice2 is {dice2}')

# for all others (4, 5, 6, 8, 9, 10), need do follow up.
else:
    while True:
        # do follow up throw.
        print(f'doing follow up throw. last round got {result}')
        win_score = result

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        result = dice1+dice2
        
        # follow up rules:
        # if same as last time, win the game.
        # if it is 7, lose game.
        # if others, need do follow up throw again.
        if result == win_score:
            print(f'You win. dice1 is {dice1}, dice2 is {dice2}')
            break
        elif result == 7:
            print(f'You lose. dice1 is {dice1}, dice2 is {dice2}')
            break


print('Game end..')
