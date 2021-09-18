
import pygame
import sys
import itertools

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
root = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Block Animation')

FPS = 20
clock = pygame.time.Clock()

sprite_list = [{'name':'block 1',
                'rect':pygame.Rect(300,200,50,100),
                'color': 'hotpink', 
                'direction':[-1,1],
                'speed':[3,5]},
               {'name':'block 2',
                'rect':pygame.Rect(500,400,100,50),
                'color': 'steelblue', 
                'direction':[1,-1],
                'speed':[7,3]},
               {'name':'block 3',
                'rect':pygame.Rect(450,150,70,70),
                'color': 'indianred', 
                'direction':[1,1],
                'speed':[9,6]}
               ]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # calculate new position for blocks
    # change direction if hit the edge.
    for s in sprite_list:
        s['rect'].left = s['rect'].left + s['speed'][0] * s['direction'][0]
        s['rect'].top = s['rect'].top + s['speed'][1] * s['direction'][1]

    permus = itertools.permutations(sprite_list, 2)
    groups = zip(*([iter(permus)]*(len(sprite_list)-1)))
    for group in groups:
        collisions = 0
        y_change = 0
        x_change = 0
        for pair in group:
            s = pair[0]
            other = pair[1]
            crop = s['rect'].clip(other['rect'])
            if crop.width != 0 or crop.height != 0:
                collisions += 1
                max_collide_x = s['speed'][0]+other['speed'][0]
                max_collide_y = s['speed'][1]+other['speed'][1]
                if crop.width > max_collide_x and crop.height <= max_collide_y:
                    # horizontal side collision
                    if (other['rect'].top - s['rect'].top) * s['direction'][1] > 0:
                        y_change += 1
                elif crop.height > max_collide_y and crop.width <= max_collide_x:
                    # vertical side collision
                    if (other['rect'].left - s['rect'].left) * s['direction'][0] > 0:
                        x_change += 1
                elif crop.height <= max_collide_y and crop.width <= max_collide_x:
                    # corner collision
                    if (other['rect'].top - s['rect'].top) * s['direction'][1] > 0:
                        y_change += 1
                    if (other['rect'].left - s['rect'].left) * s['direction'][0] > 0:
                        x_change += 1
                else:
                    # it should not happen. one frame time cannot collide so much deep.
                    print(f'{s["name"]} collide {other["name"]}, width {crop.width}, height {crop.height}') 
                    assert 0
        else:
            s['direction'][0] *= (-1)**x_change
            s['direction'][1] *= (-1)**y_change
            
    for s in sprite_list:        
        if s['rect'].left < 0:
            s['direction'][0] = 1
        elif s['rect'].right > WINDOW_WIDTH:
            s['direction'][0] = -1

        if s['rect'].top < 0:
            s['direction'][1] = 1
        elif s['rect'].bottom > WINDOW_HEIGHT:
            s['direction'][1] = -1


    root.fill('lightgreen')

    # draw blocks with new position for each frame.
    for s in sprite_list:
        pygame.draw.rect(root,s['color'],s['rect'])

    # actually show the display
    pygame.display.update()

    clock.tick(FPS)
