
import settings
import pygame


class SoundMenuObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 

        self.off_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.off_image, color, (25, 25), 20)
        self.on_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.on_image, color, (25, 25), 20)
        pygame.draw.circle(self.on_image, (255, 255, 255), (25, 25), 20, 4)
        self.clicked = False

        font = pygame.font.SysFont('Times New Roman', 32)
        self.sound_on = font.render('Sound On', False, color)
        self.sound_off = font.render("Sound Off",False,color)


        self.image = pygame.Surface((250, 70), pygame.SRCALPHA) 
        self.rect = self.image.get_rect(center = (x, y))
        self.image.blits(blit_sequence=[(self.sound_on,(10,20)),(self.on_image,(180,10))])

    def on_click(self):
        self.clicked = not self.clicked
        image,desc = (self.off_image,self.sound_off) if self.clicked else (self.on_image,self.sound_on)
        sound = settings.MUSIC_OFF if self.clicked else settings.MUSIC_ON
        self.image.fill(0)
        self.image.blits(blit_sequence=[(desc,(10,20)),(image,(180,10))])
        settings.i_queue.add([settings.I_EVENT_SOUND,sound])

class StartMenuObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 

        font = pygame.font.SysFont('Times New Roman', 32)
        text = font.render('One player start', False, color)

        self.image = pygame.Surface((250, 70), pygame.SRCALPHA) 
        self.rect = self.image.get_rect(center = (x, y))
        self.image.blit(text,(10,20))

    def on_click(self):
        settings.i_queue.add([settings.I_EVENT_GAMESTART,0])

class MenuController():
    def __init__(self,screen):
        self.group = pygame.sprite.Group([
                SoundMenuObject(screen.get_width() // 3, screen.get_height() // 3, settings.color_cyan),
                StartMenuObject(screen.get_width() // 3, screen.get_height()*2 // 3, settings.color_green)
                ])

    def on_click(self,pos):
        # get a list of all sprites that are under the mouse cursor
        clicked_menu = [s for s in self.group if s.rect.collidepoint(pos)]
        # do something with the clicked sprites...
        for s in clicked_menu:
            s.on_click()

    def draw(self,screen):
        self.group.draw(screen)


