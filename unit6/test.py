
import pygame
import sprite

root = pygame.display.set_mode((800, 600), 0, 32)
FPS = 10
clock = pygame.time.Clock()

block1 = sprite.MyBlockSprite('green',(100,100),(20,20))

group1 = pygame.sprite.Group()
group2 = pygame.sprite.RenderUpdates()
group3 = pygame.sprite.LayeredDirty()

def clear_callback(sur,rect):
    sur.fill('blue',rect)

bgd = pygame.Surface((800,600))
bgd.fill('blue')

group = group2
block1.add(group)
root.fill('black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    block1.dirty = 1
    block1.visible = 0

    areas = group.draw(root)
    print(areas)
    print(type(areas))
    pygame.display.update()
    pygame.time.wait(3000)

    block1.dirty = 1
    areas = group.clear(root, bgd)
    print(areas)
    print(type(areas))
    pygame.display.update()
    pygame.time.wait(3000)

    clock.tick(FPS)
