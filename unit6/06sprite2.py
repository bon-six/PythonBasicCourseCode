import pygame
import sys


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACK_GROUND_COLOR = 'hotpink'
FPS = 40


class MyBlockSprite(pygame.sprite.DirtySprite):
    def __init__(self,color,pos,size):    # Call the parent class (Sprite) constructor
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
        self.dirty = 1
        self.visible = 1


    def update(self, *args):
        # move the position
        self.speed_y += 1
        self.rect.left += self.speed_x * self.direction_x
        self.rect.top += self.speed_y * self.direction_y

        # check if hit the edge, if hit then reverse the moving direction (bounce)
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.direction_x *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.direction_y *= -1

        floor = args[0]
        hero_update = args[1]
        hit_floor = self.rect.colliderect(floor.rect)
        # check if need jump
        if self.speed_y == 1 and 'jump' in hero_update and hit_floor:
            self.speed_y = -16
        # check if landing floor
        elif hit_floor:
            self.rect.top = floor.rect.top - self.rect.height
            self.speed_y = 0

        self.dirty = 1
        
    def change_speed(self, sx, sy):
        self.speed_x = sx
        self.speed_y = sy

    def change_direction(self, dx, dy):
        self.direction_x = dx
        self.direction_y = dy
   
    
class MyFloorSprite(pygame.sprite.DirtySprite):
    def __init__(self,color,pos,size):    # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([size[0],size[1]])
        self.image.fill(color)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.color = color
        self.rect.topleft = pos
        self.dirty = 1
        self.visible = 1

    def update(self, *args):
        self.dirty = 0
        
   
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
        self.sprites_all = pygame.sprite.LayeredDirty()
        
        block1 = MyBlockSprite('steelblue', (100,100), (50,70))
        block1.change_speed(0,0)
        block1.change_direction(0,1)
        block1.add(self.sprites_all)

        block2 = MyFloorSprite('lightgreen', (0,500), (WINDOW_WIDTH,50))
        block2.add(self.sprites_all)

        self.floor_sprite = block2
        self.bgd = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bgd.fill(BACK_GROUND_COLOR)

    def game_loop(self):
        update_areas = []
        hero_update = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        hero_update.append('jump')

            self.sprites_all.clear(self.root, self.bgd)
            
            self.sprites_all.update(self.floor_sprite, hero_update)
            hero_update.clear()

            # LayeredDirty draw(), will check the dirty and visible flag, to decide blit()
            # improve blit() performance when have static sprites
            update_areas = self.sprites_all.draw(self.root)
            
            print(update_areas)
            # for test purpose only. check the update_areas rect.
            # it is slightly larger than the block. floor is not included. 
            # the size larger is same as speed of moving of the block.

            # update only the changed area
            # improve display performance
            pygame.display.update(update_areas)
            update_areas.clear()

            self.clock.tick(FPS)

if __name__ == '__main__':
    gc = GameController()
    gc.game_loop()
