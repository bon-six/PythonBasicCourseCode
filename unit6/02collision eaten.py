
import pygame, sys, random


def detectRectOverlap(rect1, rect2):
    for a,b in [(rect1, rect2), (rect2, rect1)]:
        if (detectPointInRect(a.topleft,b) or
            detectPointInRect(a.topright,b) or
            detectPointInRect(a.bottomleft,b) or
            detectPointInRect(a.bottomright,b) ):
            return True
    return False

def detectPointInRect(point,rect):
    x,y=point
    if (x>=rect.left  and  x<rect.right   and
        y>=rect.top   and y<rect.bottom ):
        return True
    else:
        return False


pygame.init()

# create a clock to do the game speed control.
# clock.tick() will take a frame rate argument.
clock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

MOVESPEED = 7

FOODSIZE = 20
FOODCOLOR = GREEN

bouncer = {'rect':pygame.Rect(300,100,50,50),'color':RED,'dir':[-1,-1]}
foods = []

def create_food():
    while True:
        food = pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),
                           random.randint(0,WINDOWHEIGHT-FOODSIZE),
                           FOODSIZE, FOODSIZE)
        for food_current in foods:
            if detectRectOverlap(food,food_current):
                break
        else:
            foods.append(food)
            return

new_food_timer = 20

screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Collision Detection')

for _ in range(20):
    create_food()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    bouncer['rect'].left += (MOVESPEED*(bouncer['dir'][0]))
    bouncer['rect'].top += (MOVESPEED*(bouncer['dir'][1]))

    if bouncer['rect'].top <0:
        bouncer['dir'][1] = 1
    if bouncer['rect'].bottom>WINDOWHEIGHT:
        bouncer['dir'][1] = -1
    if bouncer['rect'].left<0:
        bouncer['dir'][0] = 1
    if bouncer['rect'].right>WINDOWWIDTH:
        bouncer['dir'][0] = -1

    pygame.draw.rect(screen,bouncer['color'],bouncer['rect'])

    for food in foods:
        if detectRectOverlap(food,bouncer['rect']):
            foods.remove(food)
        else:
            pygame.draw.rect(screen,FOODCOLOR,food)

    if new_food_timer < 20:
        new_food_timer += 1
    else:
        if len(foods)<20:
            create_food()
            new_food_timer = 0
        
    pygame.display.update()

    clock.tick(40)
