import random
import sys


XLENGTH = 64
YLENGTH = 20



class GameBoard:

    def __init__(self):
        self.cell = []

    def reset_board(self):
        self.cell = [['~' for j in range(YLENGTH)] for i in range(XLENGTH)]

    def show_board(self):
        str_1 = ' '*4
        for i in range(1,7): str_1 = str_1 + ' '*9 + str(i)
        print(str_1)
        str_1 = ' '*3+'0123456789'*6+'0123'
        print(str_1)
        for j in range(YLENGTH):
            str_1 = '{0:2d}'.format(j)+' '
            for i in range (XLENGTH):
                str_1=str_1+self.cell[i][j]
            str_1=str_1+' '+'{0:2d}'.format(j)
            print(str_1)
        str_1 = ' '*3+'0123456789'*6+'0123'
        print(str_1)
        str_1 = ' '*4
        for i in range(1,7): str_1 = str_1 + ' '*9 + str(i)
        print(str_1)

    def add_detector(self,coord):
        x,y = coord
        if not 0<=x<XLENGTH :return
        if not 0<=y<YLENGTH :return
        self.cell[x][y]='d'
        
    def remove_detector(self,coord):
        x,y = coord
        if not 0<=x<XLENGTH :return
        if not 0<=y<YLENGTH :return
        if not self.cell[x][y]=='d': return
        self.cell[x][y] = '~'

    def show_chest(self,coord):
        x,y = coord
        if not 0<=x<XLENGTH :return
        if not 0<=y<YLENGTH :return
        self.cell[x][y]='c'

    def show_detected_cell(self,coord,dist):
        x,y = coord
        if not 0<=x<XLENGTH :return
        if not 0<=y<YLENGTH :return
        cell_list =[]
        if not 0<dist<10: return
        x1 = x-dist
        x2 = x+dist
        y1 = y-dist
        y2 = y+dist

        if x1<0:
            if y1<0:
                for y_iter in range(y2+1):
                    if self.cell[x2][y_iter]=='~': self.cell[x2][y_iter]=str(dist)
                for x_iter in range(x2+1):
                    if self.cell[x_iter][y2]=='~': self.cell[x_iter][y2]=str(dist)
            elif y2>YLENGTH-1:
                for y_iter in range(y1,YLENGTH):
                    if self.cell[x2][y_iter]=='~': self.cell[x2][y_iter]=str(dist)
                for x_iter in range(x2+1):
                    if self.cell[x_iter][y1]=='~': self.cell[x_iter][y1]=str(dist)
            else:
                for y_iter in range(y1,y2+1):
                    if self.cell[x2][y_iter]=='~': self.cell[x2][y_iter]=str(dist)
                for x_iter in range(x2+1):
                    if self.cell[x_iter][y1]=='~': self.cell[x_iter][y1]=str(dist)
                    if self.cell[x_iter][y2]=='~': self.cell[x_iter][y2]=str(dist)
        elif x2>XLENGTH-1:
            if y1<0:
                for y_iter in range(y2+1):
                    if self.cell[x1][y_iter]=='~': self.cell[x1][y_iter]=str(dist)
                for x_iter in range(x1,XLENGTH):
                    if self.cell[x_iter][y2]=='~': self.cell[x_iter][y2]=str(dist)
            elif y2>YLENGTH-1:
                for y_iter in range(y1,YLENGTH):
                    if self.cell[x1][y_iter]=='~': self.cell[x1][y_iter]=str(dist)
                for x_iter in range(x1,XLENGTH):
                    if self.cell[x_iter][y1]=='~': self.cell[x_iter][y1]=str(dist)
            else:
                for y_iter in range(y1,y2+1):
                    if self.cell[x1][y_iter]=='~': self.cell[x1][y_iter]=str(dist)
                for x_iter in range(x1,XLENGTH):
                    if self.cell[x_iter][y1]=='~': self.cell[x_iter][y1]=str(dist)
                    if self.cell[x_iter][y2]=='~': self.cell[x_iter][y2]=str(dist)
        else:
            if y1<0:
                for y_iter in range(y2+1):
                    if self.cell[x1][y_iter]=='~': self.cell[x1][y_iter]=str(dist)
                    if self.cell[x2][y_iter]=='~': self.cell[x2][y_iter]=str(dist)
                for x_iter in range(x1,x2+1):
                    if self.cell[x_iter][y2]=='~': self.cell[x_iter][y2]=str(dist)
            elif y2>YLENGTH-1:
                for x_iter in range(x1,x2+1):
                    if self.cell[x_iter][y1]=='~': self.cell[x_iter][y1]=str(dist)
                for y_iter in range(y1,YLENGTH):
                    if self.cell[x1][y_iter]=='~': self.cell[x1][y_iter]=str(dist)
                    if self.cell[x2][y_iter]=='~': self.cell[x2][y_iter]=str(dist)
            else:
                for x_iter in range(x1,x2+1):
                    if self.cell[x_iter][y1]=='~': self.cell[x_iter][y1]=str(dist)
                    if self.cell[x_iter][y2]=='~': self.cell[x_iter][y2]=str(dist)
                for y_iter in range(y1,y2+1):
                    if self.cell[x1][y_iter]=='~': self.cell[x1][y_iter]=str(dist)
                    if self.cell[x2][y_iter]=='~': self.cell[x2][y_iter]=str(dist)

    def remove_all_detected(self):
        for x in range(XLENGTH):
            for y in range(YLENGTH):
                if self.cell[x][y].isdigit():
                    self.cell[x][y] = '~'

class UserPlayer():
    def __init__(self):
        self.available_detector = 16
        self.used_detector = []

    def get_next_loc(self):
        print('Please give location for next detector(2 integers, 0~63, 0~15), or q to quit')
        while True:
            coord = input('>>>')
            if len(coord)==0: continue
            if coord[0] == 'q': return (-1,-1)
            if coord[0]=='h':print(gc.hidden_chest)
            coord = coord.split()
            if len(coord)!=2: continue
            if not coord[0].isdigit(): continue
            if not coord[1].isdigit(): continue
            x=int(coord[0])
            y=int(coord[1])
            if x<0 or x>XLENGTH-1 or y<0 or y>YLENGTH-1: continue
            if (x,y) in self.used_detector:
                print('the location already has a sonar working. please choose another')
                continue
            self.use_one_detector()
            self.used_detector.append((x,y))
            return (x,y)

    def use_one_detector(self):
        self.available_detector-=1


class GameController():
    def __init__(self):
        self.hidden_chest = []
        self.detected_chest = []
        
        
        self.gb = GameBoard()
        self.user = UserPlayer()

    def start_game(self):
        self.gb.reset_board()
        while len(self.hidden_chest)<3:
            x=random.randint(0,XLENGTH-1)
            y=random.randint(0,YLENGTH-1)
            if (x,y) not in self.hidden_chest:
                self.hidden_chest.append((x,y))
        self.gb.show_board()

    def exit_game(self):
        sys.exit()

    def game_loop(self):
        while self.user.available_detector>0:
            
            x,y=self.user.get_next_loc()
            if x==-1 and y==-1:
                return False
                            
            self.gb.add_detector((x,y))
            if (x,y) in self.hidden_chest:
                self.detected_chest.append((x,y))
                self.hidden_chest.remove((x,y))
                self.gb.show_chest((x,y))
                self.gb.remove_all_detected()
                if len(self.hidden_chest)==0:
                    print('You find all the treasure chest')
                    self.gb.show_board()
                    return True
                print('Found one treasure chest at ',x,y)
                print('Still have ',len(self.hidden_chest),' treasure chest to be found')
                print('Still have ',self.user.available_detector,' detectors to use')
                for x1,y1 in self.user.used_detector: #re-draw the whole board
                    for cx,cy in self.hidden_chest:
                        dist = max(abs(cx-x1),abs(cy-y1))
                        if dist<10:   #detect range maximum 9
                            self.gb.show_detected_cell((x1,y1),dist)
            else:
                print('Used ', len(self.user.used_detector),' detectors')
                print('Still have ',self.user.available_detector,' detectors to use')
                print('Still have ',len(self.hidden_chest),' chest to be found')
                for cx,cy in self.hidden_chest:  #for the need added sonar, to draw board
                    dist = max(abs(cx-x),abs(cy-y))
                    if dist<10:   #detect range maximum 9
                        self.gb.show_detected_cell((x,y),dist)

            self.gb.show_board()

        return False


if __name__=='__main__':
    gc = GameController()
    gc.start_game()
    win = gc.game_loop()
