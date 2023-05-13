import pygame
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 40
BACK_GROUND_COLOR = 'black'

class MyBlockSprite(pygame.sprite.Sprite):
    def __init__(self,color,pos,size):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # initialize any attributes needed for the sprite
        self.direction_x = -1
        self.direction_y = 1
        self.speed_x = 4
        self.speed_y = 5

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([size[0],size[1]])
        self.image.fill(color)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.color = color
        self.rect.topleft = pos

    def update(self):
        # move the position
        self.rect.left += self.speed_x * self.direction_x
        self.rect.top += self.speed_y * self.direction_y

        # check if hit the edge, if hit then reverse the moving direction (bounce)
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.direction_x *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.direction_y *= -1
        
    def change_speed(self, sx, sy):
        self.speed_x = sx
        self.speed_y = sy

    def change_direction(self, dx, dy):
        self.direction_x = dx
        self.direction_y = dy
    

class GameController():

    def __init__(self):
        pygame.init()
        self.root = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
        pygame.display.set_caption('sprite')
        self.clock = pygame.time.Clock()   
        self.root.fill(BACK_GROUND_COLOR)
        try:
            self.game_resource_init()
        except (IOError, RuntimeError, MemoryError):
            print('resource init error.')
            raise
        except Exception:
            print('resource init error.')
            raise
        except:
            print('unknown error')
            pygame.quit()
            sys.exit()

    def game_resource_init(self):
        self.sprites_all = pygame.sprite.RenderUpdates()
        self.update_areas = []

        block1 = MyBlockSprite('steelblue', (100,400), (50,70))
        block1.change_speed(5,7)
        block1.add(self.sprites_all)

        block2 = MyBlockSprite('indianred', (500,250), (70,50))
        block2.change_direction(-1,-1)
        block2.add(self.sprites_all)

    @staticmethod
    def clear_callback(sur,rect):
        sur.fill(BACK_GROUND_COLOR,rect)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # clear the current sprite, replace with background
            self.sprites_all.clear(self.root, GameController.clear_callback)
            
            # update all sprites. group update will call to each sprite update()
            self.sprites_all.update()
            
            # the RenderUpdates group draw() will return the list of rects which have changes.
            self.update_areas = self.sprites_all.draw(self.root)

            print(self.update_areas) 
            # this print() is for test purpose only. 
            # check the update_area rect, it is slightly larger than the block size. 
            # compare with speed, will find it is one frame movement size larger.

            # update display, with the changed areas to be updated.
            # improve display performance.
            pygame.display.update(self.update_areas)
            self.update_areas.clear()

            self.clock.tick(FPS)

if __name__ == '__main__':
    gc = GameController()
    gc.game_loop()
