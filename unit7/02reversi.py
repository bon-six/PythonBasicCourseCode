import sys

class GameBoard :

    DIRECTIONS = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

    def __init__ (self):
        super().__init__()
        self.moves = [[' ' for i in range(8)] for j in range(8)]
        self.moves[3][3],self.moves[4][4]='X','X'
        self.moves[3][4],self.moves[4][3]='O','O'

    def reset_moves(self):
        self.__init__()

    def render_board(self):
        print('    0   1   2   3   4   5   6   7')
        for j in range(8):
            print('   '+'   |'*7)
            str_1=f'{j:2d} '
            for i in range(7):
                str_1=str_1+' '+self.moves[i][j]+' '+'|'
            str_1=str_1+' '+self.moves[7][j]
            print(str_1)
            print('   '+'   |'*7)
            if j!=7:
                print('-'*34)

    def get_allneighbours(self):
        neighbours = []
        for i in range(8):
            for j in range(8):
                if self.moves[i][j] == ' ':
                    for change_x, change_y in self.DIRECTIONS:
                        new_x = i+change_x
                        new_y = j+change_y
                        if new_x>7 or new_x<0 or new_y>7 or new_y<0:
                            continue
                        if self.moves[new_x][new_y] != ' ':
                            neighbours.append((i,j))
                            break
        return neighbours
    '''
    def get_allneighbours(self):
        neighbours = []
        for i in range(8):
            for j in range(8):
                if self.moves[i][j] != ' ':
                    for change_x, change_y in self.DIRECTIONS:
                        new_x = i+change_x
                        new_y = j+change_y
                        if new_x>7 or new_x<0 or new_y>7 or new_y<0:
                            continue
                        if self.moves[new_x][new_y] == ' ':
                            if (new_x,new_y) not in neighbours:
                                neighbours.append((new_x,new_y))
        return neighbours
    '''
    def check_cell_flip(self, cell, player):
        flips = []
        opponent = 'X' if player=='O' else 'O'
        for change_x, change_y in self.DIRECTIONS:
            check_x = cell[0]+change_x
            check_y = cell[1]+change_y
            if check_x<0 or check_x>7 or check_y<0 or check_y>7:
                continue
            if self.moves[check_x][check_y] == opponent:
                # this direction has opponents to check.
                find = 0
                while True:
                    check_x+=change_x
                    check_y+=change_y
                    if check_x<0 or check_x>7 or check_y< 0 or check_y>7 or \
                        self.moves[check_x][check_y] == ' ':
                        break
                    elif self.moves[check_x][check_y] == opponent:
                        continue
                    elif self.moves[check_x][check_y] == player:
                        find=1
                        break
                if find ==1:
                    while (check_x, check_y) != cell:
                        check_x -= change_x
                        check_y -= change_y
                        flips.append((check_x, check_y))
        return (None if not flips else flips)
            
    def get_hints(self,player):
        hints = []
        neighbours = self.get_allneighbours()
        if not neighbours: return None
        for x,y in neighbours:
            if (self.check_cell_flip((x,y), player)):
                hints.append((x,y))
        return (None if not hints else hints)

    def show_hints(self,hints):
        if not hints: return
        for x,y in hints:
            if self.moves[x][y] != ' ':
                return
        for x,y in hints:
            self.moves[x][y] = '-'
        self.render_board()

    def remove_hints(self,hints):
        if not hints: return
        for x,y in hints:
            if self.moves[x][y] != '-':
                return
        for x,y in hints:
            self.moves[x][y] = ' '

    def check_valid_move(self,coord,player):
        hints = self.get_hints(player)
        if hints == None:
            return False
        elif coord in hints:
            return True
        return False

    def add_move(self,coord,player):
        x,y = coord
        if x<0 or x>7: return
        if y<0 or y>7: return
        if self.moves[x][y]!=' ': return
        self.moves[x][y]=player
        flip_cells=self.check_cell_flip(coord, player)
        assert flip_cells
        for flip_x,flip_y in flip_cells:
            self.moves[flip_x][flip_y]=player
        return


class Player :
    def __init__(self, player=' '):
        super().__init__()
        self.player = player
        self.skipped = False

    def next_move(self):
        pass


class ComputerPlayer (Player):
    def __init__ (self, gb, player):
        super().__init__(player)
        self.gb = gb

    @staticmethod
    def check_corner_move(cell_list):
        corner_list = []
        for x,y in cell_list:
            if x in [0,7] and y in [0,7]:
                corner_list.append((x,y))
        if len(corner_list)==0: return None
        return corner_list

    @staticmethod
    def check_side_move(cell_list):
        side_list=[]
        for x,y in cell_list:
            if (x in [0,7] and y not in [0,7]) or (y in [0,7] and x not in [0,7]):
                side_list.append((x,y))
        if len(side_list)==0: return None
        return side_list

    def next_move(self):
        hints=self.gb.get_hints(self.player)
        if hints==None:
            print('Computer player no valid move. skipped')
            self.skipped = True
            return None
        max_flips = 0
        max_cell =(-1,-1)

        check_func_list = [self.check_corner_move,self.check_side_move,lambda hints:hints]

        for check_func in check_func_list:
            tmp_moves = check_func(hints)
            if tmp_moves==None: continue
            for x,y in tmp_moves:
                flip_list = self.gb.check_cell_flip((x,y),self.player)
                if len(flip_list)>max_flips:
                    max_cell = (x,y)
                    max_flips = len(flip_list)
            self.skipped = False
            return max_cell
        else:
            assert False


class UserPlayer (Player) :
    def __init__ (self, gb):
        super().__init__()
        self.gb = gb
        while self.player != 'X' and self.player != 'O':
            self.player = input("please choose your player side 'X', or 'O'.\n>>>")

    def next_move(self):
        hints = self.gb.get_hints(self.player)
        if hints == None:
            print('You have no valid move! Skipped')
            self.skipped = True
            return None
        while True:
            answer = input('Your next move: q to quit, h for hints. 2 integers of 0~7 for next move\n>>>')
            if len(answer)>0:
                if answer[0] == 'q':
                    sys.exit()
                elif answer[0] == 'h':
                    # show hints to user
                    self.gb.show_hints(hints)
                    self.gb.remove_hints(hints)
                else:
                    answer =answer.split()
                    if len(answer)==2 and answer[0].isdecimal() and answer[1].isdecimal():
                        x = int(answer[0])
                        y = int(answer[1])
                        if ( 0<=x<=7 and 0<=y<=7):
                            if (self.gb.check_valid_move((x,y), self.player)):
                                self.skipped = False
                                return(x,y)
                            else:
                                print('the cell location you wanted is not valid')

class GameController:
    def __init__(self):
        self.gb = GameBoard()
        self.game_end = False
        self.user = UserPlayer(self.gb)
        self.computer = ComputerPlayer(self.gb, 'X' if self.user.player=='O' else 'O')

    def restart_game(self):
        self.gb.reset_moves()
        self.game_end = False

    def game_loop(self):
        # let 'X' be the first mover.
        mover = self.user if self.user.player == 'X' else self.computer
        
        previous_mover = None
        self.gb.render_board()

        while not self.game_end:
            next_move = mover.next_move()
            if next_move == None:
                if previous_mover.skipped:
                    self.game_end = True
                    break  # two player both no more move. game end
            else:
                self.gb.add_move(next_move,mover.player)
                if mover == self.computer:
                    input('===computer finished one move===press enter to continue')
                self.gb.render_board()

            # switch player
            previous_mover = mover
            mover = self.computer if mover == self.user else self.user

        # no more moves,game end
        o_score=0
        x_score=0
        for i in range(8):
            for j in range(8):
                if self.gb.moves[i][j]=='X':
                    x_score+=1
                else:
                    o_score+=1
        return(x_score,o_score)

if __name__ == '__main__':
    gc = GameController()
    while True:
        score = gc.game_loop()

        print(f'Player X get score {score[0]:2d}')
        print(f'Player O get score {score[1]:2d}')

        answer = input('Do you want play again?(yes/no)>>>')
        if (answer == 'yes' or answer == 'y'):
            gc.restart_game()
            continue
        #game end
        break
