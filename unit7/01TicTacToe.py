
import random

class GameBoard :

    def __init__ (self):
        self.moves = [[' ' for i in range(3)] for j in range(3)]

    def reset_moves(self):
        self.__init__()

    def render_board(self):
        print('   |   |')
        print(' '+self.moves[0][0]+' '+'|'+' '+self.moves[1][0]+' '+'|'+' '+self.moves[2][0])
        print('   |   |')
        print('===========')
        print('   |   |')
        print(' '+self.moves[0][1]+' '+'|'+' '+self.moves[1][1]+' '+'|'+' '+self.moves[2][1])
        print('   |   |')
        print('===========')
        print('   |   |')
        print(' '+self.moves[0][2]+' '+'|'+' '+self.moves[1][2]+' '+'|'+' '+self.moves[2][2])
        print('   |   |')

    def check_space_free(self, coord):
        x,y = coord
        if (x<0 or x>2 or y<0 or y>2) :
            return False
        return (self.moves[x][y] == ' ')

    def add_move(self, player, coord):
        if player != 'X' and player != 'O':
            return None
        x,y = coord
        if (x<0 or x>2 or y<0 or y>2) :
            return None
        self.moves[x][y] = player
        return True

    def get_allmoves(self):
        return self.moves

    def check_win(self, player):
        # check rows for win.
        for i in range(3):
            if self.moves[i].count(player) == 3:
                return True
        # check columns for win
        for i in range(3):
            tmp_list = [self.moves[0][i],self.moves[1][i],self.moves[2][i]]
            if tmp_list.count(player) == 3:
                return True
        # check diagonal for win
        tmp_list = [self.moves[0][0],self.moves[1][1],self.moves[2][2]]
        if tmp_list.count(player) == 3:
            return True
        tmp_list = [self.moves[0][2],self.moves[1][1],self.moves[2][0]]
        if tmp_list.count(player) == 3:
            return True

        return False

    def check_space_full(self):
        for i in range(3):
            for j in range(3):
                if self.moves[i][j] == ' ':
                    return False
        return True


class Player :
    def __init__(self, player=' '):
        self.player = player

    def next_move(self):
        pass


class ComputerPlayer (Player):
    def __init__ (self, gb, player):
        super().__init__(player)
        self.gb = gb
        
    def find_onemove_win(self, current_move):
        for i in range(3):
            tmp_list = current_move[i]
            if tmp_list.count(self.player) == 2 and tmp_list.count(' ') == 1 :
                return (i,tmp_list.index(' '))
        for i in range(3):
            tmp_list = [current_move[0][i],current_move[1][i],current_move[2][i]]
            if tmp_list.count(self.player)==2 and tmp_list.count(' ')==1 :
                return (tmp_list.index(' '),i)
        tmp_list = [current_move[0][0],current_move[1][1],current_move[2][2]]
        if tmp_list.count(self.player)==2 and tmp_list.count(' ')==1 :
            i = tmp_list.index(' ')
            return (i,i)
        tmp_list = [current_move[0][2],current_move[1][1],current_move[2][0]]
        if tmp_list.count(self.player)==2 and tmp_list.count(' ')==1 :
            i = tmp_list.index(' ')
            return (i,2-i)
        return None

    def find_onemove_lose(self,current_move):
        tmp_player = self.player
        self.player = 'O' if self.player == 'X' else 'X'
        coord = self.find_onemove_win(current_move)
        self.player = tmp_player
        return coord

    def find_corner_move(self,current_moves):
        tmp_list=[]
        for x in [0,2]:
            for y in [0,2]:
                if current_moves[x][y] == ' ':
                    tmp_list.append((x,y))
        empty_cell = len(tmp_list)
        if empty_cell == 0:
            return None
        return tmp_list[random.randint(0, empty_cell-1)]

    def find_center_move(self,current_moves):
        if current_moves[1][1] == ' ':
            return((1,1))
        else:
            return None

    def find_side_move(self,current_moves):
        tmp_list=[(0,1),(1,0),(0,2),(2,0)]
        for x,y in tmp_list:
            if current_moves[0][1] != ' ':
                tmp_list.remove((x,y))
        empty_cell = len(tmp_list)
        if empty_cell == 0:
            return None
        return tmp_list[random.randint(0,empty_cell-1)]
        
    def find_random_move(self, current_moves):
        tmp_list =[]
        for x in range(3):
            for y in range(3):
                if current_moves[x][y]==' ':
                    tmp_list.append((x,y))
        empty_cell = len(tmp_list)
        if empty_cell == 0:
            return None
        return tmp_list[random.randint(0,empty_cell-1)]
        
    def next_move(self):
        current_moves = self.gb.get_allmoves() 
        coord = self.find_onemove_win(current_moves)
        if (coord!=None ):
            return coord
        coord = self.find_onemove_lose(current_moves)
        if (coord!=None):
            return coord
        coord = self.find_center_move(current_moves)
        if (coord!=None):
            return coord
        coord = self.find_corner_move(current_moves)
        if (coord!=None):
            return coord
        coord = self.find_side_move(current_moves)
        if (coord!=None):
            return coord
        return None

'''
    def next_move(self):
        current_moves = self.gb.get_allmoves() 
        coord = self.find_random_move(current_moves)
        return coord
'''

class UserPlayer (Player) :
    def __init__ (self, gb):
        super().__init__()
        self.gb = gb
        while self.player != 'X' and self.player != 'O':
            self.player = input("please choose your player side 'X', or 'O'.>>>")

    def next_move(self):
        coord = None
        while coord == None:
            next_step = input('Please give your next move(X Y)>>>')
            next_move = next_step.split()
            if len(next_move) == 2 and next_move[0].isdecimal() and next_move[1].isdecimal():
                next_move[0] = int(next_move[0])
                next_move[1] = int(next_move[1])
                if 0<=next_move[0]<3 and 0<=next_move[1]<3:
                    coord = (next_move[0],next_move[1])
                    if (self.gb.check_space_free(coord)):
                        return coord
                    else:
                        print('invalid move.')
                        coord = None

class GameController:
    def __init__(self):
        self.gb = GameBoard()
        self.user = UserPlayer(self.gb)
        computer = 'X' if self.user.player == 'O' else 'O'
        self.computer = ComputerPlayer(self.gb, computer)

    def restart_game(self):
        self.gb.reset_moves()
        
    def game_loop(self):
        # decide who is the first mover for this game. 0 means computer, 1 means user.
        mover = random.randint(0,1)
        mover = self.computer if mover == 0 else self.user

        self.gb.render_board()

        while not self.gb.check_space_full():
            next_move = mover.next_move()
            if next_move == None:
                break

            self.gb.add_move(mover.player, next_move)
            if mover == self.computer:
                print ('===computer finished one move===')
            self.gb.render_board()
            if self.gb.check_win(mover.player):
                return mover.player

            # switch player
            mover = self.computer if mover == self.user else self.user

        # game board full no space, no one win, the game end in draw
        return ' '


if __name__ == '__main__':
    gc = GameController()
    score = 0

    while True:
        winner = gc.game_loop()
        if winner == gc.user.player:
            print('You win the game.')
            score+=1
        elif winner == gc.computer.player:
            print('Computer win the game.')
        else:
            print('the game end in draw')
            
        answer = input('Do you want play again?(yes/no)>>>')
        if answer == 'y' or answer == 'yes':
            gc.restart_game()
        #game end
        else:
            break

    print(f'You win {score:d} games')
