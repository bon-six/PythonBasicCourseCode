
import pygame, sys, random
import pathlib

pygame.init()

FPS = 40
clock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
surRoot = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Sprite & Sound')

path = pathlib.Path('D:/Edu/program_resource')

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

MOVESPEED = 4

PLAYERSIZE = 40
player_image = pygame.image.load(path/'sprite'/'Pac-Man.png')
player = {'rect':player_image.get_rect(),'dir':[0,0]}

ratio = max(player['rect'].size)//PLAYERSIZE
player['rect'].size = (player['rect'].width//ratio,player['rect'].height//ratio)
player['rect'].topleft = (random.randint(0,WINDOWWIDTH-player['rect'].width),
                    random.randint(0,WINDOWHEIGHT-player['rect'].height))
player_stretched = pygame.transform.scale(player_image,player['rect'].size)


FOODSIZE = 10
foods = []
food_image = pygame.image.load(path/'sprite'/'Yellow_icon.png')
food_image = pygame.transform.scale(food_image,(FOODSIZE,FOODSIZE))
special_food_image = pygame.image.load(path/'sprite'/'ghost-icon-14-256.png')
special_food_image = pygame.transform.scale(special_food_image,(FOODSIZE,FOODSIZE))

def create_random_food():
    while True:
        food = pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),
                           random.randint(0,WINDOWHEIGHT-FOODSIZE),
                           FOODSIZE, FOODSIZE)
        for food_current in foods:
            if food_current.colliderect(food):
                break
            if player['rect'].colliderect(food):
                break
        else:
            foods.append(food)
            return food
    
for i in range(20):
    create_random_food()

special_foods=[]
score = 0

new_food_timer = 20

pick_sound = pygame.mixer.Sound(path/'music'/'mixkit-arcade-retro-game-over-213.wav')
pygame.mixer.music.load(path/'music'/'instrumental_for_studying_house_music.mp3')
pygame.mixer.music.play(-1,0.0)
music_playing = True

done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
            break
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
                done = True
                break
            if event.key == ord('m'):
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                music_playing = not music_playing
        if event.type == pygame.MOUSEBUTTONUP:
            food = pygame.Rect(event.pos[0],event.pos[1],FOODSIZE,FOODSIZE)
            special_foods.append(food)

    surRoot.fill(BLACK)

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

    last_score = score

    if new_food_timer < 20:
        new_food_timer += 1
    else:
        if len(foods)<20:
            food = create_random_food()
            new_food_timer = 0

    for food in foods:
        if food.colliderect(player['rect']):
            foods.remove(food)
            score += 2
            if music_playing:
                pick_sound.play()
        

    for food in special_foods:
        if food.colliderect(player['rect']):
            special_foods.remove(food)
            score = 0 if score-5<=0 else score-5

    inflate = score - last_score
    player['rect'].width += inflate
    player['rect'].height += inflate
    player_stretched= pygame.transform.scale(player_image,player['rect'].size)  
    
    for food in foods: surRoot.blit(food_image,food)
    for food in special_foods: surRoot.blit(special_food_image,food)
    surRoot.blit(player_stretched,player['rect'])
    
    pygame.display.update()

    clock.tick(FPS)

# Game done.
pygame.quit()
sys.exit()
