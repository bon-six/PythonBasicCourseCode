
import pygame, sys, math

pygame.init()
clock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

FPS = 60

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

MOVESPEED = 4

b1 = {'id':0,'rect':pygame.Rect(300,80,100,50),'color':RED,'dir':[-1,1]}
b2 = {'id':1,'rect':pygame.Rect(150,200,30,60),'color':GREEN,'dir':[1,-1]}


blocks=[b1,b2]

screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation')


def move(b):
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

def collision_bounce(a,b):
    b_top = a['rect'].clipline(b['rect'].topleft, b['rect'].topright)
    b_left = a['rect'].clipline(b['rect'].topleft, b['rect'].bottomleft)
    b_right = a['rect'].clipline(b['rect'].topright, b['rect'].bottomright)
    b_bottom = a['rect'].clipline(b['rect'].bottomleft, b['rect'].bottomright)

    if (not b_top) and (not b_left) and (not b_right) and (not b_bottom):
        return

    top_line = 0
    left_line = 0
    right_line = 0
    bottom_line = 0

    if b_top:
        top_line = math.hypot(b_top[0][0]-b_top[1][0], b_top[0][1]-b_top[1][1])
    if b_left:
        left_line = math.hypot(b_left[0][0]-b_left[1][0], b_left[0][1]-b_left[1][1])
    if b_right:
        right_line = math.hypot(b_right[0][0]-b_right[1][0], b_right[0][1]-b_right[1][1])
    if b_bottom:
        bottom_line = math.hypot(b_bottom[0][0]-b_bottom[1][0], b_bottom[0][1]-b_bottom[1][1])

    if  top_line > MOVESPEED:
        if a['dir'][1] == 1 and b['dir'][1] == -1:
            a['dir'][1] = -1
            b['dir'][1] = 1
    elif  left_line > MOVESPEED:
        if a['dir'][0] == 1 and b['dir'][0] == -1:
            a['dir'][0] = -1
            b['dir'][0] = 1
    elif right_line > MOVESPEED:
        if a['dir'][0] == -1 and b['dir'][0] == 1:
            a['dir'][0] = 1
            b['dir'][0] = -1
    elif bottom_line > MOVESPEED:
        if a['dir'][1] == -1 and b['dir'][1] == 1:
            a['dir'][1] = 1
            b['dir'][1] = -1
    elif top_line > 0 and left_line > 0:
        if a['dir'][0] == 1 and b['dir'][0] == -1 and a['dir'][1] == 1 and b['dir'][1] == -1:
            a['dir'][0] = -1
            b['dir'][0] = 1
            a['dir'][1] = -1
            b['dir'][1] = 1
    elif top_line > 0 and right_line > 0:
        if a['dir'][0] == -1 and b['dir'][0] == 1 and a['dir'][1] == 1 and b['dir'][1] == -1:
            a['dir'][1] = -1
            b['dir'][1] = 1
            a['dir'][0] = 1
            b['dir'][0] = -1
    elif bottom_line > 0 and left_line > 0:
        if a['dir'][0] == 1 and b['dir'][0] == -1 and a['dir'][1] == -1 and b['dir'][1] == 1:
            a['dir'][0] = -1
            b['dir'][0] = 1
            a['dir'][1] = 1
            b['dir'][1] = -1
    elif bottom_line > 0 and right_line > 0:
        if a['dir'][0] == -1 and b['dir'][0] == 1 and a['dir'][1] == -1 and b['dir'][1] == 1:
            a['dir'][0] = 1
            b['dir'][0] = -1
            a['dir'][1] = 1
            b['dir'][1] = -1
            

if __name__ == "__main__":
    print ("started")
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_on = False
                break

        if not game_on:
            break

        screen.fill(BLACK)
        
        for b in blocks:
            move(b)

        collision_bounce(b1,b2)


        for b in blocks:
            pygame.draw.rect(screen,b['color'], b['rect'])

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
