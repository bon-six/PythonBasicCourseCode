
import pygame, sys, random

pygame.init()

# create a clock to do the game speed control.
# clock.tick() will take a framerate argument.
clock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

MOVESPEED = 4

FOODSIZE = 20
FOODCOLOR = GREEN

PLAYERSIZE = 50
player = {'rect':pygame.Rect(300,100,PLAYERSIZE,PLAYERSIZE),'color':WHITE,'dir':[0,0]}
foods = []

def create_random_food():
    while True:
        food = pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),
                           random.randint(0,WINDOWHEIGHT-FOODSIZE),
                           FOODSIZE, FOODSIZE)
        for food_current in foods:
            if food_current.colliderect(food):
                break
        else:
            foods.append(food)
            return food
    
for i in range(20):
    create_random_food()

new_food_timer = 20

surRoot = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Event Processing')

SPECIAL_FOOD_COLOR=BLUE
special_foods=[]

while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player['dir'][0]=-1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player['dir'][0]=1
            if event.key == pygame.K_UP or event.key == ord('w'):
                player['dir'][1]=-1
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player['dir'][1]=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if player['dir'][0]==-1: player['dir'][0]=0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if player['dir'][0]==1: player['dir'][0]=0
            if event.key == pygame.K_UP or event.key == ord('w'):
                if player['dir'][1]==-1: player['dir'][1]=0
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if player['dir'][1]==1: player['dir'][1]=0
            if event.key == ord('x'):
                player['rect'].top = random.randint(0,WINDOWHEIGHT-PLAYERSIZE)
                player['rect'].left = random.randint(0,WINDOWWIDTH-PLAYERSIZE)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            food = pygame.Rect(event.pos[0],event.pos[1],FOODSIZE,FOODSIZE)
            special_foods.append(food)
            

    player['rect'].left += MOVESPEED*player['dir'][0]
    player['rect'].top += MOVESPEED*player['dir'][1]

    if player['rect'].top <0:
        player['rect'].top = 0
    if player['rect'].bottom>WINDOWHEIGHT:
        player['rect'].bottom = WINDOWHEIGHT
    if player['rect'].left<0:
        player['rect'].left = 0
    if player['rect'].right>WINDOWWIDTH:
        player['rect'].right = WINDOWWIDTH

    if new_food_timer < 20:
        new_food_timer += 1
    else:
        if len(foods)<20:
            food = create_random_food()
            new_food_timer = 0

    surRoot.fill(BLACK)
    
    pygame.draw.rect(surRoot,player['color'],player['rect'])

    for food in foods:
        if food.colliderect(player['rect']):
            foods.remove(food)
        else:
            pygame.draw.rect(surRoot,FOODCOLOR,food)

    for food in special_foods:
        if food.colliderect(player['rect']):
            special_foods.remove(food)
        else:
            pygame.draw.rect(surRoot,SPECIAL_FOOD_COLOR,food)

    pygame.display.update()

    clock.tick(40)
