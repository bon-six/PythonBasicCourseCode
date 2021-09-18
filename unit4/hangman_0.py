
import random


HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


WORDS_DICTIONARY = '''ant cat dog bee room file flower apple panda seal letter
fish shark park zoo water field salmon beef turtle whale pen mouse bug never lose
news paper knife fork goat duck fox lion tiger banana pear papaya pine tree deer cow
rabbit python wolf cloth shoes and spider spin run walk smooth move kick store wave
shine wind rain sun moon rose lotus tulip daisy carrot corn cucumber pepper grow
become stay taste turn see appear feel sound able calm bad easy fair half gentle kind
faint bare more less worse much little quick that can verb smile cry joke sea land rock
sand some good what else too simple end start lock open will never hold talk loud quite
list top bottom right left side effect nice well white black pink red blue orange purple
green yellow silver gold'''.split()



def reset_game():
    global identified_letters
    global secret
    global hang_parts
    # generate the secret word. initialize the guessed letter as empty
    secret = WORDS_DICTIONARY[random.randint(0,len(WORDS_DICTIONARY))]
    identified_letters = ['_']*len(secret)

    # initialize the hangman body part start from 0
    hang_parts = 0


def show_game_prompt():
    print(HANGMANPICS[hang_parts])
    print(''.join(identified_letters))

def check_new_letter(new_letter):
    for i in range (len(secret)):
        if new_letter == secret[i] and identified_letters[i] == '_':
            return i   # new guess letter match to i position of secret
    return -1   # new guess letter not match

def add_identified(new_letter,position):
    identified_letters[position] = new_letter
    if '_' in identified_letters:
        return 1  #still have letters not identified
    else:
        return 2   #all letters has been identified


def add_hangman_parts():
    global hang_parts
    hang_parts += 1
    if hang_parts == 6:
        return -1   # hangman finished. all parts hang already
    else:
        return 0   # still have parts.



secret=''
identified_letters=[]
hang_parts=0
score=0

reset_game()

game_on = True
while game_on :
    show_game_prompt()

    new_letter = input('Please give a guess which letter is in my secret word.>>>')
    new_letter = new_letter[0]  # take only one letter guess for one round
    new_letter = new_letter.lower()

    pos = check_new_letter(new_letter)
    discovered_this_guess = 0;
    while pos != -1 :
        discovered_this_guess += 1
        finished = add_identified(new_letter,pos)
        if finished == 2:
            print('Congratulations. Secret all revealed.')
            score+=1
            show_game_prompt()
            answer = input('Do you want play one more time?>>>')
            if answer == 'yes' or answer == 'y':
                # play game again with new secret
                reset_game()
            else:
                game_on = False
            break
        else:
            pos = check_new_letter(new_letter)

    if (pos == -1):
        if (discovered_this_guess > 0):
            print('Well done. you get one letter from my secret.')
            discovered_this_guess = 0
            continue
        else:
            print('guess wrong. letter not in my secret.')
            game_over = add_hangman_parts()
            if game_over == -1:
                print('Uh-oh. game over.')
                show_game_prompt()
                print('my secret is {0:s}'.format(''.join(secret)))
                answer = input('Do you want play one more time?>>>')
                if answer == 'yes' or answer == 'y':
                    # play game again with new secret
                    reset_game()
                else:
                    game_on = False
                    
        
print(f'You win {score:d} times')
