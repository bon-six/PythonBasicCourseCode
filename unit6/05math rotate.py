import pygame

pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)


BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

center = (200,200)

pygame.draw.line(screen, GREEN, (center[0]-20, center[1]), (center[0]+20, center[1]), 2)
pygame.draw.line(screen, GREEN, (center[0], center[1]-20), (center[0], center[1]+20), 2)
pygame.draw.circle(screen, GREEN, (center[0], center[1]), 7, 0)

p = (100,0)

p = pygame.math.Vector2(p)

pygame.draw.circle(screen, RED, (center[0]+p[0], center[1]+p[1]), 5, 0)

p = p.rotate(90)

pygame.draw.circle(screen, YELLOW, (center[0]+p[0], center[1]+p[1]), 5, 0)

pygame.display.update()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done = True


pygame.quit()    
