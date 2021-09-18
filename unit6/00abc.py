
import pygame
import sys


pygame.init()

WINDOWS_SIZE=(800,600)

FPS=40

screen = pygame.display.set_mode(WINDOWS_SIZE,0,32)
pygame.display.set_caption('program title')

clock = pygame.time.Clock()

# load all necessary resources, like image, sound, etc.

while True:  # game loop

    # process all events that need to respond, mouse, keyboard
    # command from player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP : # other event process code
            pass

    # draw background
    screen.fill(WHITE)

    # move or action of the sprite


    # any picture changed, then reflect it onto the screen.
    # screen.blit()

    # draw the result into the screen
    pygame.display.flip()
    # or pygame.display.update().
    # update function can draw only part of the screen

    clock.tick(FPS)
    
    
