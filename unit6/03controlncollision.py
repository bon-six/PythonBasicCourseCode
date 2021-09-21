
import pygame, sys, random

pygame.init()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Move and Eat!')

clock = pygame.time.Clock()

FOODSIZE = 20
FOODCOLOR = 'green'
TOTAL_FOOD = 10

block1 = {'rect':pygame.Rect(300,100,50,50),
          'color':'red',
          'dir':[0,0],
          'speed':[11,7]}
foods = []
def create_food():
    while True:
        food = pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),
                           random.randint(0,WINDOWHEIGHT-FOODSIZE),
                           FOODSIZE, FOODSIZE)
        for food_current in foods:
            if food_current.colliderect(food):
                break
        else:
            foods.append(food)
            return

new_food_timer = 20

for _ in range(TOTAL_FOOD):
    create_food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if block1['dir'][1] != 1:
                    block1['dir'][1] = -1
            elif event.key == pygame.K_DOWN:
                if block1['dir'][1] != -1:
                    block1['dir'][1] = 1
            elif event.key == pygame.K_LEFT:
                if block1['dir'][0] != 1:
                    block1['dir'][0] = -1
            elif event.key == pygame.K_RIGHT:
                if block1['dir'][0] != -1:
                    block1['dir'][0] = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if block1['dir'][1] != 1:
                    block1['dir'][1] = 0
            elif event.key == pygame.K_DOWN:
                if block1['dir'][1] != -1:
                    block1['dir'][1] = 0
            elif event.key == pygame.K_LEFT:
                if block1['dir'][0] != 1:
                    block1['dir'][0] = 0
            elif event.key == pygame.K_RIGHT:
                if block1['dir'][0] != -1:
                    block1['dir'][0] = 0

    screen.fill('black')

    block1['rect'].left += (block1['speed'][0]*(block1['dir'][0]))
    block1['rect'].top += (block1['speed'][1]*(block1['dir'][1]))

    eaten = 0
    for food in foods:
        if food.colliderect(block1['rect']):
            foods.remove(food)
            eaten += 1
        else:
            pygame.draw.rect(screen,FOODCOLOR,food)

    if eaten > 0:
        block1['rect'].height += eaten
        block1['rect'].width += eaten
        eaten = 0

    if (block1['rect'].left < 0):
        block1['rect'].left = 0
    if (block1['rect'].top < 0):
        block1['rect'].top = 0
    if (block1['rect'].right > WINDOWWIDTH):
        block1['rect'].right = WINDOWWIDTH
    if (block1['rect'].bottom > WINDOWHEIGHT):
        block1['rect'].bottom = WINDOWHEIGHT

    pygame.draw.rect(screen, block1['color'], block1['rect'])

    if new_food_timer < 20:
        new_food_timer += 1
    else:
        if len(foods)<TOTAL_FOOD:
            create_food()
            new_food_timer = 0
        
    pygame.display.update()

    clock.tick(40)
