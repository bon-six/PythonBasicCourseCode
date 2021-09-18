

import pygame

import settings
import menu
import game
import mixer

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
pygame.display.set_caption('TETRIS GAME')
clock = pygame.time.Clock()


settings.init()
menu = menu.MenuController(screen)
game = game.GameControl(screen)
sound = mixer.MusicControl()

while True:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if settings.game_state !='menu': continue
            #menu state, process mouse event for settings
            menu.on_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and event.mod & pygame.KMOD_ALT:
                pygame.quit()
                exit()
            else:
                game.on_key_press(event)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_F4 and event.mod & pygame.KMOD_ALT:
                pass
            else:
                game.on_key_press(event)
    
    
    for event in settings.i_queue.get():
        if event[0] == settings.I_EVENT_SOUND:
            if event[1] == settings.MUSIC_ON:
                sound.start_background_music()
            elif event[1] == settings.MUSIC_OFF:
                sound.stop_background_music()
            elif event[1] == settings.SOUND_BLOCK_DOWN:
                sound.play_land_sound()
            elif event[1] == settings.SOUND_BLOCK_REMOVE:
                sound.play_remove_sound()
        
        if event[0] == settings.I_EVENT_GAMESTART:
            #game start 
            settings.game_state = 'run'
            game.start()
        if event[0] == settings.I_EVENT_GAMEPAUSE:
            settings.game_state = 'pause'
            game.pause()
        if event[0] == settings.I_EVENT_GAMESTOP or event[0] == settings.I_EVENT_GAMEOVER:
            settings.game_state = 'menu'
            game.stop()
        if event[0] == settings.I_EVENT_EXIT:
            pygame.quit()
            exit()
    if settings.game_state=='run':
        game.update()

    screen.fill((128,128,128))
    if settings.game_state == 'menu':
        menu.draw(screen)
    if settings.game_state == 'pause' or settings.game_state == 'run':
        game.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()
