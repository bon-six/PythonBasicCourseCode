
import random

class Hangman:

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

    def __init__ (self):
        self.hang_parts = 0

    def reset (self):
        self.__init__()

    def add_parts(self):
        self.hang_parts += 1
        if self.hang_parts == 6:
            return -1   # hangman finished. all parts hang already
        else:
            return 0   # still have parts not hang.

    def __str__(self):
        return(self.HANGMANPICS[self.hang_parts])


class SecretKeeper:

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

    def __init__ (self):
        self.secret = self.WORDS_DICTIONARY[random.randint(0,len(self.WORDS_DICTIONARY))]
        self.identified_letters = ['_']*len(self.secret)

    def reset_secret(self):
        self.__init__()

    def add_identified(self,new_letter,position):
        self.identified_letters[position] = new_letter
        if '_' in self.identified_letters:
            return 1  #still have letters not identified
        else:
            return 2   #all letters has been identified
    
    def check_new_letter(self,new_letter):
        for i in range (len(self.secret)):
            if new_letter == self.secret[i] and self.identified_letters[i] == '_':
                return i   # new guess letter match to i position of secret
        return -1   # new guess letter not match

    def __str__(self):
        return(''.join(self.identified_letters))

class GameController:

    def __init__(self):
        self.hangman = Hangman()
        self.secret_keeper = SecretKeeper()
        self.game_on = False
        self.score = 0

    def start_game(self):
        self.game_on=True

    def replay_game(self):
        self.secret_keeper.reset_secret()
        self.hangman.reset()

    def exit_game(self):
        self.game_on=False

    def show_promts(self):
        print(self.hangman)
        print(self.secret_keeper)
        

    def game_loop(self):
        self.start_game()
        while self.game_on :
            self.show_promts()
            new_letter = input('Please give a guess which letter is in my secret word.>>>')
            new_letter = new_letter[0]  # take only one letter guess for one round
            new_letter = new_letter.lower()

            pos = self.secret_keeper.check_new_letter(new_letter)
            discovered_this_guess = 0
            while pos != -1 :
                discovered_this_guess += 1
                finished = self.secret_keeper.add_identified(new_letter,pos)
                if finished == 2:
                    print('Congratulations. Secret all revealed.')
                    self.show_promts()
                    self.score+=1
                    answer = input('Do you want play one more time?>>>')
                    if answer == 'yes' or answer == 'y':
                        # play game again with new secret
                        self.replay_game()
                    else:
                        self.exit_game()
                    break
                else:
                    pos = self.secret_keeper.check_new_letter(new_letter)

            if (pos == -1):
                if (discovered_this_guess > 0):
                    print('Well done. you get one letter from my secret.')
                    discovered_this_guess = 0
                    continue
                else:
                    print('guess wrong. letter not in my secret.')
                    game_over = self.hangman.add_parts()
                    if game_over == -1:
                        print('Uh-oh. game over.')
                        self.show_promts()
                        print('my secret is {0:s}'.format(''.join(self.secret_keeper.secret)))
                        answer = input('Do you want play one more time?>>>')
                        if answer == 'yes' or answer == 'y':
                            # play game again with new secret
                            self.replay_game()
                        else:
                            self.exit_game()
                        
            
        return self.score
        
        
if __name__ == '__main__' :
    gc = GameController()
    score = gc.game_loop()
    print(f'You win {score:d} times')
