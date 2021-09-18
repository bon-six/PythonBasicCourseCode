
import pygame, sys, random
import pathlib

pygame.init()
clockMain = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

FPS=40


path = pathlib.Path('D:/Edu/program_resource')

PLAYERSIZE = 40
PLAYERSPEED = 5
player_image = pygame.image.load(path/'sprite'/'player ship.png')
player = {'rect':player_image.get_rect(),'dir':[0,0]}

ratio = max(player['rect'].size)//PLAYERSIZE
player['rect'].size = (player['rect'].width//ratio,player['rect'].height//ratio)
player['rect'].topleft = (random.randint(0,WINDOWWIDTH-player['rect'].width),
                    random.randint(0,WINDOWHEIGHT-player['rect'].height))
player_stretched = pygame.transform.scale(player_image,player['rect'].size)


BADDIESIZE = 20
baddies = []

imageBaddie = pygame.image.load(path/'sprite'/'axeDouble.png')
rectBaddie = imageBaddie.get_rect()
ratio = max(rectBaddie.size)//BADDIESIZE
rectBaddie.size = (rectBaddie.width//ratio,rectBaddie.height//ratio)
imageBaddie = pygame.transform.scale(imageBaddie,rectBaddie.size)
baddies.append({'image':imageBaddie,'rect':rectBaddie,'speed':0,'damage':5})

imageBaddie = pygame.image.load(path/'sprite'/'upg_sword.png')
rectBaddie = imageBaddie.get_rect()
ratio = max(rectBaddie.size)//BADDIESIZE
rectBaddie.size = (rectBaddie.width//ratio,rectBaddie.height//ratio)
imageBaddie = pygame.transform.scale(imageBaddie,rectBaddie.size)
baddies.append({'image':imageBaddie,'rect':rectBaddie,'speed':0,'damage':2})

new_baddie_timer = 5


hit_sound = pygame.mixer.Sound(path/'music'/'mixkit-arcade-retro-game-over-213.wav')
pygame.mixer.music.load(path/'music'/'instrumental_for_studying_house_music.mp3')

font = pygame.font.SysFont('arial',32)

def draw_text(text,surface,x,y):
    surText = font.render(text,1,BLACK)
    rectText = surText.get_rect()
    rectText.topleft = (x,y)
    surface.blit(surText,rectText)

screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('DODGER')


attack_baddies =[]
player_life=100
music_playing=True

def terminate():
    pygame.quit()
    sys.exit()


def main_menu():
    global music_playing
    key_press = False
    while not key_press:
        screen.fill(WHITE)
        draw_text('DODGER',screen, WINDOWWIDTH//3,WINDOWHEIGHT//3)
        draw_text('s key to start game',screen, WINDOWWIDTH//3-30,WINDOWHEIGHT//3+50)
        draw_text('m key for music on off',screen, WINDOWWIDTH//3-30,WINDOWHEIGHT//3+80)
        draw_text('ESC to exit...',screen, WINDOWWIDTH//3-30,WINDOWHEIGHT//3+110)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                elif event.key == ord('s'):
                    key_press = True
                    break;
                elif event.key == ord('m'):
                    if music_playing:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1,0.0)
                    music_playing = not music_playing

def wait_user_start():                    
    key_press = False
    while not key_press:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                else:
                    key_press = True
                    break;    

def game_intro():
    global attack_baddies, player_life
    attack_baddies=[]
    player_life = 100

    pygame.mouse.set_visible(False)
    
    if music_playing == True:
        pygame.mixer.music.play(-1,0.0)
    
    screen.fill(WHITE)
    draw_text('DODGER',screen, WINDOWWIDTH//3,WINDOWHEIGHT//3)
    draw_text('press any key to start...',screen, WINDOWWIDTH//3-30,WINDOWHEIGHT//3+50)
    draw_text('or ESC to exit...',screen, WINDOWWIDTH//3-30,WINDOWHEIGHT//3+80)
    pygame.display.flip()
    wait_user_start()
    main_menu()

def game_outtro():
    global attack_baddies, player_life
    pygame.mouse.set_visible(True)

    if music_playing == True:
        pygame.mixer.music.play(-1,0.0)

    screen.fill(WHITE)
    draw_text('GAME OVER',screen, WINDOWWIDTH//3,WINDOWHEIGHT//3)
    draw_text('press ESC to exit...',screen, WINDOWWIDTH//3-30,WINDOWHEIGHT//3+50)
    draw_text('or any other key to restart...',screen, WINDOWWIDTH//3-30,WINDOWHEIGHT//3+80)
    pygame.display.flip()

    attack_baddies=[]
    player_life = 100
    wait_user_start()


game_intro()

while True:
    
    while player_life>0:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                terminate()
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
                if event.key == pygame.K_ESCAPE:
                    terminate()
                if event.key == ord('m'):
                    if music_playing:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1,0.0)
                    music_playing = not music_playing
            if event.type == pygame.MOUSEMOTION:
                player['rect'].move_ip(event.pos[0]-player['rect'].centerx,
                                       event.pos[1]-player['rect'].centery)



        if player['dir'][0]==-1:
            player['rect'].left -= PLAYERSPEED
        elif  player['dir'][0]==1:
            player['rect'].left += PLAYERSPEED

        if  player['dir'][1]==-1:
            player['rect'].top -= PLAYERSPEED
        elif  player['dir'][1]==1:
            player['rect'].top += PLAYERSPEED

        if player['rect'].top <0:
            player['rect'].top = 0
        if player['rect'].bottom>WINDOWHEIGHT:
            player['rect'].bottom = WINDOWHEIGHT
        if player['rect'].left<0:
            player['rect'].left = 0
        if player['rect'].right>WINDOWWIDTH:
            player['rect'].right = WINDOWWIDTH

        pygame.mouse.set_pos(player['rect'].centerx,player['rect'].centery)

        if new_baddie_timer < 5:
            new_baddie_timer += 1
        else:
            if len(attack_baddies)<60:
                baddie_speed = random.randint(4,15)
                baddie_size = random.randint(-10,10)
                baddie_class = random.randint(0,1)
                baddie_rect = pygame.Rect(baddies[baddie_class]['rect'])
                ratio = baddie_size/BADDIESIZE
                w_inflate = int(baddies[baddie_class]['rect'].width*ratio)
                h_inflate = int(baddies[baddie_class]['rect'].height*ratio)
                baddie_rect.inflate_ip(w_inflate,h_inflate)
                baddie_rect.top = 0
                baddie_rect.left = random.randint(0,WINDOWWIDTH-baddie_rect.width)
                baddie_image = pygame.transform.scale(baddies[baddie_class]['image'],baddie_rect.size)
                attack_baddies.append({'image':baddie_image,
                                       'rect':baddie_rect,
                                       'speed':baddie_speed,
                                       'damage':baddies[baddie_class]['damage']})
                new_baddie_timer = 0

        for baddie in attack_baddies:
            baddie['rect'].top += baddie['speed']
            if baddie['rect'].top>WINDOWHEIGHT:
                attack_baddies.remove(baddie)
            if baddie['rect'].colliderect(player['rect']):
                player_life -= baddie['damage']
                attack_baddies.remove(baddie)
                if music_playing: hit_sound.play()
                if player_life <=0:
                    break;
                

        screen.fill(WHITE)
        draw_text('LIFE {0:d}'.format(player_life),screen,10,10)
        for baddie in attack_baddies: screen.blit(baddie['image'],baddie['rect'])
        screen.blit(player_stretched,player['rect'])
        
        pygame.display.flip()

        clockMain.tick(FPS)

    game_outtro()
