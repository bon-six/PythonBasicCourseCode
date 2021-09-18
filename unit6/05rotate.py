import pygame
import pygame.font

pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def blitRotate(surf, image, pos, pivot, angle):

#pygame math rotate is clockwise. but pygame transform rotate is counter-clockwise.
#so here use the -angle in math vector rotate, to make it same counter-clockwise rotation.

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, h), (0, h)]]
    box_rotate = [p.rotate(-angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    new_size = (max_box[0]-min_box[0], max_box[1]-min_box[1])
    min_box = pygame.math.Vector2(min_box)
    
    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(pivot[0], pivot[1])
    pivot_rotate = pivot.rotate(-angle)

    # move the rotated box, so that the center is kept same positiom
    origin = min_box + pivot - pivot_rotate


    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # blit the rotated image at pos
    new_pos = (pos[0]+origin[0], pos[1]+origin[1])
    surf.blit(rotated_image, new_pos)

    # draw rectangle around the image
    pygame.draw.rect (surf, (255, 0, 0), (new_pos, new_size),1)


font = pygame.font.SysFont('Times New Roman', 50)
text = font.render('image', False, (255, 255, 0))
image = pygame.Surface((text.get_width()+1, text.get_height()+1))
pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
image.blit(text, (1, 1))



angle = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done = True

    screen.fill(0)          

    # the place where we want image to show.
    pos = (200, 200)
    w, h = image.get_size()
    pivot = (w/2,h/2)

    # rotated_image = pygame.transform.rotate(image, angle)
    # screen.blit(rotated_image, pos)
    blitRotate(screen, image, pos, pivot, angle)
    
    angle += 1

    abs_pivot = (pos[0]+pivot[0],pos[1]+pivot[1])

    pygame.draw.line(screen, (0, 255, 0), (abs_pivot[0]-20, abs_pivot[1]), (abs_pivot[0]+20, abs_pivot[1]), 2)
    pygame.draw.line(screen, (0, 255, 0), (abs_pivot[0], abs_pivot[1]-20), (abs_pivot[0], abs_pivot[1]+20), 2)
    pygame.draw.circle(screen, (0, 255, 0), (abs_pivot[0], abs_pivot[1]), 7, 0)

    pygame.display.flip()

pygame.quit()
