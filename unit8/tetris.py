
import random
import pygame

import settings

FIGURE = {'-': [(0, 0), (1, 0), (2, 0), (3, 0)],
          'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
          'L': [(0, 0), (0, 1), (1, 1), (2, 1)],
          'J': [(2, 0), (0, 1), (1, 1), (2, 1)],
          'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
          'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
          'T': [(0, 0), (1, 0), (2, 0), (1, 1)]}

COLORS = {'-': (50, 90, 90),
          'O': (150, 0, 0),
          'L': (0, 150, 0),
          'J': (0, 0, 150),
          'Z': (150, 150, 0),
          'S': (0, 150, 150),
          'T': (150, 0, 150)}

ROTATE = {'-^':('->', [(0, 0), (0, 1), (0, 2), (0, 3)], (2,-1) ),
          '->':('-^', [(0, 0), (1, 0), (2, 0), (3, 0)], (-2,1) ),
          'O^':('O^', [(0, 0), (1, 0), (0, 1), (1, 1)], (0,0)  ), 
          'L^':('L>', [(0, 0), (1, 0), (0, 1), (0, 2)], (0,0)  ),
          'L>':('Lv', [(0, 0), (1, 0), (2, 0), (2, 1)], (-1,0) ),
          'Lv':('L<', [(1, 0), (1, 1), (0, 2), (1, 2)], (1,-1) ),
          'L<':('L^', [(0, 0), (0, 1), (1, 1), (2, 1)], (0,1) ),
          'J^':('J>', [(0, 0), (0, 1), (0, 2), (1, 2)], (1,-1) ),
          'J>':('Jv', [(0, 0), (1, 0), (2, 0), (0, 1)], (0,1) ),
          'Jv':('J<', [(0, 0), (1, 0), (1, 1), (1, 2)], (0,0) ),
          'J<':('J^', [(2, 0), (0, 1), (1, 1), (2, 1)], (-1,0) ),
          'Z^':('Z>', [(1, 0), (0, 1), (1, 1), (0, 2)], (0,-1) ),
          'Z>':('Z^', [(0, 0), (1, 0), (1, 1), (2, 1)], (0,1)  ),
          'S^':('S>', [(0, 0), (0, 1), (1, 1), (1, 2)], (0,-1) ),
          'S>':('S^', [(1, 0), (2, 0), (0, 1), (1, 1)], (0,1)  ),
          'T^':('T>', [(1, 0), (0, 1), (1, 1), (1, 2)], (0,-1) ),
          'T>':('Tv', [(1, 0), (0, 1), (1, 1), (2, 1)], (0,0) ),
          'Tv':('T<', [(0, 0), (0, 1), (1, 1), (0, 2)], (1,0) ),
          'T<':('T^', [(0, 0), (1, 0), (2, 0), (1, 1)], (-1,1) ) }


BOTTOMS = {'-': [(0, 1), (1, 1), (2, 1), (3, 1)],
           'O': [(0, 2), (1, 2)],
           'L': [(0, 2), (1, 2), (2, 2)],
           'J': [(0, 2), (1, 2), (2, 2)],
           'Z': [(1, 2), (2, 2)],
           'S': [(0, 2), (1, 2)],
           'T': [(0, 1), (2, 1), (1, 2)]}

class NextBlockObject(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.figure_images = {}
        self.figure_rects = {}
        for figure in '-OLJZST':
            minx = min([FIGURE[figure][i][0] for i in range(4)])
            maxx = max([FIGURE[figure][i][0] for i in range(4)])
            miny = min([FIGURE[figure][i][1] for i in range(4)])
            maxy = max([FIGURE[figure][i][1] for i in range(4)])
            image = pygame.Surface((settings.BLOCK_SIZE*(maxx-minx+1)//2, settings.BLOCK_SIZE*(maxy-miny+1)//2), pygame.SRCALPHA)
            block_image = pygame.Surface((settings.BLOCK_SIZE//2, settings.BLOCK_SIZE//2), pygame.SRCALPHA)
            block_image.fill(COLORS[figure])
            pygame.draw.rect(block_image, settings.color_grey, (0,0,settings.BLOCK_SIZE//2,settings.BLOCK_SIZE//2), 1)
            image.blits(blit_sequence=[(block_image,((i-minx)*settings.BLOCK_SIZE//2,(j-miny)*settings.BLOCK_SIZE//2)) for (i,j) in FIGURE[figure]])
            self.figure_images[figure]=image
            self.figure_rects[figure] = image.get_rect(center=(x,y))
        self.figure=None
        self.image=None
        self.rect=None
    def set_next(self,figure):
        self.figure = figure
        self.image = self.figure_images[figure]
        self.rect = self.figure_rects[figure]

class WellObject(pygame.sprite.Sprite):
    def __init__(self, x,y, color):
        super().__init__() 
        font = pygame.font.SysFont('Times New Roman', 24)
        self.image = pygame.Surface((settings.BLOCK_SIZE*10, settings.BLOCK_SIZE*20), pygame.SRCALPHA)
        self.block_image = pygame.Surface((settings.BLOCK_SIZE, settings.BLOCK_SIZE), pygame.SRCALPHA)
        self.block_image.fill(color)
        pygame.draw.rect(self.block_image, settings.color_grey, (0,0,settings.BLOCK_SIZE,settings.BLOCK_SIZE), 1)
        self.image.blits(blit_sequence=[(self.block_image,(i,j)) for i in range(0,settings.BLOCK_SIZE*10,settings.BLOCK_SIZE) 
                                                                 for j in range(0,settings.BLOCK_SIZE*20,settings.BLOCK_SIZE)])
        self.rect = self.image.get_rect(center=(x,y))
        self.grid = [[None for j in range(20)] for i in range(10)]
        #create figure colored block images for future use
        self.figure_images = {}
        for figure in '-OLJZST':
            image = pygame.Surface((settings.BLOCK_SIZE, settings.BLOCK_SIZE), pygame.SRCALPHA)
            image.fill(COLORS[figure])
            pygame.draw.rect(image, settings.color_grey, (0,0,settings.BLOCK_SIZE,settings.BLOCK_SIZE), 1)
            self.figure_images[figure]=image

    def update_well(self):
        sequence = []
        for i in range(10):
            for j in range(20):
                if self.grid[i][j] is None:
                    image = self.block_image
                else:
                    image = self.figure_images[self.grid[i][j]]
                sequence.append((image,(settings.BLOCK_SIZE*i,settings.BLOCK_SIZE*j)))
        self.image.blits(blit_sequence=sequence)


    def detect_collision(self,block):
        for i in range(4):
            if block.pos[0]+block.blocks[i][0]<0 or block.pos[0]+block.blocks[i][0]>9:
                return 1
            if block.pos[1]+block.blocks[i][1]>19:
                return 1
        for i in range(4):
            if block.pos[1]+block.blocks[i][1]<0:
                continue
            if self.grid[block.pos[0]+block.blocks[i][0]][block.pos[1]+block.blocks[i][1]] is not None:
                return 1
        return 0

    def update_grid(self,block):
        for i in range(4):
            if block.pos[1]+block.blocks[i][1] < 0: continue 
            self.grid[block.pos[0]+block.blocks[i][0]][block.pos[1]+block.blocks[i][1]]=block.figure[0]

    def remove_grid(self,block):
        for i in range(4):
            if block.pos[1]+block.blocks[i][1] < 0: continue 
            self.grid[block.pos[0]+block.blocks[i][0]][block.pos[1]+block.blocks[i][1]]=None

    def reset_grid(self):
        self.grid = [[None for j in range(20)] for i in range(10)]

    def remove_grid_row(self,row):
        if row>0:
            for j in range(row-1,-1,-1):
                for i in range(0,10):
                    self.grid[i][j+1]=self.grid[i][j]
        for i in range(0,10):
            self.grid[i][0]=None

    def check_full_row(self):
        rows=[]
        for j in range(20):
            test=True
            for i in range(10):
                test=bool(self.grid[i][j]) and test
                if not test:
                    break
            if not test:
                continue
            else:
                rows.append(j)
        for j in rows:
            self.remove_grid_row(j)
        
        if len(rows) == 0:
            settings.i_queue.add([settings.I_EVENT_SOUND,settings.SOUND_BLOCK_DOWN])
        else:
            settings.i_queue.add([settings.I_EVENT_SOUND,settings.SOUND_BLOCK_REMOVE])
            if len(rows) == 1:
                settings.game_score+=10
            elif len(rows) == 2:
                settings.game_score+=30
            elif len(rows)==3:
                settings.game_score+=60
            elif len(rows)==4:
                settings.game_score+=100
        
        if settings.game_score>3000:
            settings.game_level=1


class Tetris():
    def __init__(self):
        self.figure = None
        self.blocks = None
        self.well = None

    def reset(self,figure,well_obj):
        if figure == '-':
            self.pos = (3,-1)
        else:
            self.pos = (4,-2)
        self.figure = figure+'^'
        self.blocks = FIGURE[figure]
        self.well = well_obj

    @classmethod
    def generate_one(cls):
        return '-OLJZST'[random.randint(0,6)]

    def move_down(self):
        if self.pos[1]>=0 and self.pos[1]+max([self.blocks[i][1] for i in range(4)])==19:
            self.well.check_full_row()
            return -1 # block landed at well bottom.
        
        original_pos = self.pos
        self.well.remove_grid(self)
        self.pos = (self.pos[0],self.pos[1]+1)
        if self.well.detect_collision(self):
            self.pos=original_pos
            self.well.update_grid(self)
            self.well.check_full_row()
            return -1   # this block landed need process next.
        else:
            self.well.update_grid(self)
            return 0   # this block continue dropping.
        pass

    def rotate(self):
        original_pos = self.pos
        original_blocks = self.blocks
        original_figure = self.figure
        self.well.remove_grid(self)
        self.figure,self.blocks,pos = ROTATE[self.figure]
        self.pos = (self.pos[0]+pos[0],self.pos[1]+pos[1])
        if self.well.detect_collision(self):
            self.pos=original_pos
            self.blocks=original_blocks
            self.figure=original_figure
            self.well.update_grid(self)
            return -1
        else:
            self.well.update_grid(self)
            return 0
        pass

    def move_left(self):
        original_pos = self.pos
        self.well.remove_grid(self)
        self.pos=(self.pos[0]-1,self.pos[1])
        if self.well.detect_collision(self):
            self.pos=original_pos
            self.well.update_grid(self)
            return -1
        else:
            self.well.update_grid(self)
            return 0
        pass
    
    def move_right(self):
        original_pos = self.pos
        self.well.remove_grid(self)
        self.pos=(self.pos[0]+1,self.pos[1])
        if self.well.detect_collision(self):
            self.pos=original_pos
            self.well.update_grid(self)
            return -1
        else:
            self.well.update_grid(self)
            return 0
        pass
