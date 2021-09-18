import random

# start the game
print('''I have a secret number, 3 digits. Please take a guess what it is.
I will give you hint each time you guess
Fermi -- one digit is correct and in the exact position
Pico  -- one digit is correct but in wrong position
Bagel -- one digit is not correct''')

score = 0  # used for recording how many times success.

# start the game loop
while True:
    secret_number = [str(i) for i in range(10)]
    random.shuffle(secret_number)
    # if first digit is '0', ramdomly put it to second or third position
    if (secret_number[0] == '0'):
        i = random.randint(1,2)
        secret_number[i], secret_number[0] = secret_number[0], secret_number[i]
        
    # only keep the first 3 digits as secret
    for i in range(9,2,-1):
        del secret_number[i]

    # the game loop maximum 10 times for one secret guess.
    for guess_round in range(10):
        answer = input('Please give your guess.\n>>>')
        # check the answer if it's valid and store it in guess[]
        if len(answer) != 3:
            print('Please give me 3 digits exactly')
            continue
        guess = list(answer)
        if not all(map(lambda x: x.isdecimal(), guess)):
            print('Please give only decimal digits')
            continue
        # compose hint
        hint = ''
        for i in range(3):
            if secret_number[i] == guess[i]:
                hint +='Fermi '
            elif secret_number[i] in guess:
                hint +='Pico '
            else:
                hint +='Bagel '
        #remove the positional relation of the hint to secret
        hint = hint.split()
        hint.sort(reverse=True)
        hint = ' '.join(hint)
        print(hint)
        if hint == 'Fermi Fermi Fermi':
            print('You got it!!!')
            score+=1
            break
    else: 
        print('You failed guess the number within 10 times.')

    answer = input('Do you want play again? (y to continue)\n>>>')
    if len(answer) == 0 or (answer[0] != 'y' and answer[0] != 'Y'):
        break

print(f'You successfully guess the number for {score:d} times.')