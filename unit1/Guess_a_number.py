
# a guess the number game

import random

# to record how many guesses have done.
guesses_taken = 0


user_name = input('Hello! What is your name?>>>')

number = random.randint(1,20)

print('Welcome,', user_name)
print('I have a number between 1 to 20. Please take a guess what I have')

not_done = True

while not_done:
    guess = input ('Give me your guess.>>>')
    guesses_taken += 1

    if guess.isdigit():
        guess = int(guess)
        if guess == number:
# find the correct number. stop the game.
            print('Great!! You did the job.')
            print('You take',guesses_taken,'times to guess the number.')
            break
        elif guess > number:
            print('Your guess is too high')
        else:
            print('Your guess is too low')
    else:
        print('guess wrong')

# after 5 times guess still not get it, stop the game.
    if guesses_taken == 5:
        print('You missed. The number I had was', number)
        break

print('Game End!')
        
    
