
import pygame, sys

WINDOWWIDTH = 800
WINDOWHEIGHT= 600

WINDOWSIZE = (WINDOWWIDTH, WINDOWHEIGHT)

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

FPS = 20

pygame.init()
screen = pygame.display.set_mode(WINDOWSIZE,0,32)
pygame.display.set_caption('Test')

clock = pygame.time.Clock()

tr = 255
show = 1

sur1 = pygame.Surface((50,50))
rect1 = pygame.Rect(0,0,50,50)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    
    if tr == 0:
        tr += 1
        show = 1
    elif tr == 255:
        tr -=1
        show = -1
    elif show == 1:
        tr +=1
    elif show == -1:
        tr-=1

    sur1.set_alpha(tr)
    color1 = RED
    color2 = GREEN
    color3 = BLUE
    pygame.draw.rect(sur1,color1,rect1)
    screen.blit(sur1,(200,300))
    pygame.draw.rect(sur1,color2,rect1)
    screen.blit(sur1,(400,300))
    pygame.draw.rect(sur1,color3,rect1)
    screen.blit(sur1,(600,300))


    pygame.display.update()
    clock.tick(FPS)

    
