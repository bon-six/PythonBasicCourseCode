

import pygame

import settings
import tetris

class GameInfoObject(pygame.sprite.Sprite):
    def __init__(self,screen,text1,text2, color):
        super().__init__() 
        font = pygame.font.SysFont('Times New Roman', 72)
        sur1 = font.render(text1, False, color)
        font = pygame.font.SysFont('Times New Roman', 24)
        sur2 = font.render(text2, False, color)
        self.image = pygame.Surface((600, 200), pygame.SRCALPHA)
        self.image.blits(blit_sequence=[(sur1,(150,10)),(sur2,(150,150))])
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2))

class TextObject(pygame.sprite.Sprite):
    def __init__(self, text, x,y, color):
        super().__init__() 
        font = pygame.font.SysFont('Times New Roman', 24)
        self.image = font.render(text, False, color)
        self.rect = self.image.get_rect(center = (x,y))

class NumberObject(pygame.sprite.Sprite):
    def __init__(self,value, x,y, color):
        super().__init__()
        self.value = value
        self.color=color
        self.center=(x,y)
        self.font = pygame.font.SysFont('Times New Roman', 24)
        self.image = self.font.render(str(value), False, color)
        self.rect = self.image.get_rect(center = (x,y))
    def set_value(self,value):
        self.value=value
        self.image = self.font.render(str(self.value), False, self.color)
        self.rect = self.image.get_rect(center = self.center)
    

class GameControl():
    def __init__(self,screen):
        self.group_to_draw = []
        self.pause_obj = GameInfoObject(screen,'PAUSE','SPACE to continue, q to leave', settings.color_cyan)
        self.score_text_obj = TextObject('score', screen.get_width() //4, screen.get_height() - settings.BLOCK_SIZE*20-50, settings.color_black)
        self.score_obj = NumberObject(0,screen.get_width() //4, screen.get_height() - settings.BLOCK_SIZE*20-25, settings.color_cyan)
        self.level_text_obj = TextObject('level', screen.get_width() *3 //4, screen.get_height() - settings.BLOCK_SIZE*20-50, settings.color_black)
        self.level_obj = NumberObject(0,screen.get_width()*3 //4, screen.get_height() - settings.BLOCK_SIZE*20-25, settings.color_cyan)
        self.well_obj = tetris.WellObject(300,500,settings.color_black)
        self.future_piece = tetris.Tetris.generate_one()
        self.future_block = tetris.NextBlockObject(screen.get_width()//2, screen.get_height() - settings.BLOCK_SIZE*20-30)
        self.future_block.set_next(self.future_piece)
        self.falling_figure = None
        self.falling_obj=tetris.Tetris()
        self.game_counts=0
        self.rotate_hold=False
        self.rotate_stroke = False
        self.right_hold=False
        self.right_stroke = False
        self.left_hold =False
        self.left_stroke=False
        self.down_hold=False
        self.down_stroke=False
        pass
        

    def start(self):
        self.game_counts = settings.GAME_ONE_STEP_COUNTS
        pass

    def pause(self):
        pass

    def stop(self):
        self.future_piece=tetris.Tetris.generate_one()
        self.future_block.set_next(self.future_piece)
        self.falling_figure = None
        self.well_obj.reset_grid()
        settings.game_level = 0
        settings.game_score = 0
        pass

    def update(self):
        if settings.game_state != 'run': return
        if self.falling_figure == None:
            self.falling_figure = self.future_piece
            self.falling_obj.reset(self.falling_figure,self.well_obj)
            if self.falling_obj.move_down()==-1:
                settings.i_queue.add([settings.I_EVENT_GAMEOVER,0])  # game over.
                return
            self.future_piece = tetris.Tetris.generate_one()
            self.future_block.set_next(self.future_piece)
        
        if self.game_counts < settings.GAME_ONE_STEP_COUNTS - settings.game_level*10:
            self.game_counts+=1
            return
        self.game_counts=0
        if self.rotate_stroke:
            self.rotate_stroke = False
            self.falling_obj.rotate()
        
        if self.right_stroke and not self.left_stroke:
            self.right_stroke = False
            self.falling_obj.move_right()
        elif self.left_stroke and not self.right_stroke:
            self.left_stroke=False
            self.falling_obj.move_left()
        elif self.left_stroke and self.right_stroke:
            self.right_stroke = False
            self.left_stroke=False

        if self.down_hold: # press key down give additional move down accelaration
            if self.falling_obj.move_down() == -1:
                self.falling_figure = None
            elif self.falling_obj.move_down() == -1:
                self.falling_figure = None
        if self.falling_figure!=None:
            if self.falling_obj.move_down() == -1:
                self.falling_figure = None

        self.well_obj.update_well()
        self.score_obj.set_value(settings.game_score)
        self.level_obj.set_value(settings.game_level)
        pass

    def on_key_press(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if settings.game_state == 'menu':
                    settings.i_queue.add([settings.I_EVENT_EXIT,0])
            elif event.key == pygame.K_SPACE:  
                if settings.game_state == 'run':
                    settings.i_queue.add([settings.I_EVENT_GAMEPAUSE,0])
                elif settings.game_state == 'pause':
                    settings.i_queue.add([settings.I_EVENT_GAMESTART,0])
            elif event.key == ord('q') or event.key == ord('Q') :  
                if settings.game_state == 'pause':
                    settings.i_queue.add([settings.I_EVENT_GAMESTOP,0])
            elif event.key == pygame.K_UP:  
                if settings.game_state != 'run': return
                self.rotate_hold=True
                pass
            elif event.key == pygame.K_RIGHT:  
                if settings.game_state != 'run': return
                self.right_hold=True
                pass
            elif event.key == pygame.K_LEFT:  
                if settings.game_state != 'run': return
                self.left_hold =True
                pass
            elif event.key == pygame.K_DOWN:  
                if settings.game_state != 'run': return
                self.down_hold=True
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:  
                if settings.game_state != 'run': return
                self.rotate_hold = False
                self.rotate_stroke = True
                pass
            elif event.key == pygame.K_RIGHT:  
                if settings.game_state != 'run': return
                self.right_hold=False
                self.right_stroke = True
                pass
            elif event.key == pygame.K_LEFT:  
                if settings.game_state != 'run': return
                self.left_hold=False
                self.left_stroke=True
                pass
            elif event.key == pygame.K_DOWN:  
                if settings.game_state != 'run': return
                self.down_hold=False
                self.down_stroke=True
                pass
                


    def draw(self,screen):
        if settings.game_state == 'pause':
            self.group_to_draw = pygame.sprite.Group([self.pause_obj])
            self.group_to_draw.draw(screen)
        if settings.game_state == 'run':
            self.group_to_draw = pygame.sprite.Group([self.score_text_obj, 
                                              self.level_text_obj, 
                                              self.score_obj, 
                                              self.level_obj, 
                                              self.well_obj,
                                              self.future_block])
            self.group_to_draw.draw(screen)
