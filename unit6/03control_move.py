
import pygame
import sys
import itertools

pygame.init()


WINDOW_SIZE = (800,600)
root = pygame.display.set_mode(WINDOW_SIZE,0,32)
pygame.display.set_caption('Events control')

FPS = 40
clock = pygame.time.Clock()

blocks = [{'name': 'block1',
           'color': 'lightgreen',
           'rect': pygame.Rect(300, 200, 100, 50),
           'speed': [3, 4],
           'direction': [0, 0]},
          ]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if blocks[0]['direction'][1] != 1:
                    blocks[0]['direction'][1] = -1
            elif event.key == pygame.K_DOWN:
                if blocks[0]['direction'][1] != -1:
                    blocks[0]['direction'][1] = 1
            elif event.key == pygame.K_LEFT:
                if blocks[0]['direction'][0] != 1:
                    blocks[0]['direction'][0] = -1
            elif event.key == pygame.K_RIGHT:
                if blocks[0]['direction'][0] != -1:
                    blocks[0]['direction'][0] = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if blocks[0]['direction'][1] != 1:
                    blocks[0]['direction'][1] = 0
            elif event.key == pygame.K_DOWN:
                if blocks[0]['direction'][1] != -1:
                    blocks[0]['direction'][1] = 0
            elif event.key == pygame.K_LEFT:
                if blocks[0]['direction'][0] != 1:
                    blocks[0]['direction'][0] = 0
            elif event.key == pygame.K_RIGHT:
                if blocks[0]['direction'][0] != -1:
                    blocks[0]['direction'][0] = 0

    for block in blocks:
        block['rect'].left += (block['speed'][0] * block['direction'][0])
        block['rect'].top += (block['speed'][1] * block['direction'][1])

    for block in blocks:
        if (block['rect'].left < 0):
            block['rect'].left = 0
        if (block['rect'].top < 0):
            block['rect'].top = 0
        if (block['rect'].right > WINDOW_SIZE[0]):
            block['rect'].right = WINDOW_SIZE[0]
        if (block['rect'].bottom > WINDOW_SIZE[1]):
            block['rect'].bottom = WINDOW_SIZE[1]

    root.fill('hotpink')

    pygame.draw.rect(root, blocks[0]['color'], blocks[0]['rect'])

    pygame.display.update()

    clock.tick(FPS)
