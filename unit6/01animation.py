
import pygame, sys, time

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

MOVESPEED = 4

b1 = {'rect':pygame.Rect(300,80,50,100),'color':RED,'dir':[-1,1]}
b2 = {'rect':pygame.Rect(200,200,20,20),'color':GREEN,'dir':[-1,-1]}
b3={'rect':pygame.Rect(100,150,60,60),'color':BLUE,'dir':[1,-1]}

blocks=[b1,b2,b3]

screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation')

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    for b in blocks:
        if b['dir'][0]==-1:
            b['rect'].left -= MOVESPEED
        elif  b['dir'][0]==1:
            b['rect'].left += MOVESPEED

        if  b['dir'][1]==-1:
            b['rect'].top -= MOVESPEED
        elif  b['dir'][1]==1:
            b['rect'].top += MOVESPEED

        if b['rect'].top <0:
            b['dir'][1] = 1
        if b['rect'].bottom>WINDOWHEIGHT:
            b['dir'][1] = -1
        if b['rect'].left<0:
            b['dir'][0] = 1
        if b['rect'].right>WINDOWWIDTH:
            b['dir'][0] = -1

        pygame.draw.rect(screen,b['color'],b['rect'])

    pygame.display.update()
    time.sleep(0.02)
