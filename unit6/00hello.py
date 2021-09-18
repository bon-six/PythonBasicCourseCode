# we must import pygame module in order to use all the pygame functions to create out game program.
import pygame
import sys

# each time, must call pygame.init() before using any other pygame functions.
# and every pygame program when exit, must call pygame.quit() before leave.
pygame.init()

# Surface is an object type that can draw things on it.
# here we use pygame display module to create the program main window Surface.
# set_mode function will take a (width, height) tuple as first parameter and return the Surface object
# set_caption will set the program title.
screen = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello World!')

# constants we use for colors.
# pygame use 3 integers tuple to define different colors
# first number gives how many red, secord number gives how many green,
# and the third color gives how many blue.
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

# fill function draw all pixels of the Surface. we make all pixels WHITE.
screen.fill(WHITE)

# draw different shapes in the Surface (surRoot, the main window)
# draw polygon, need pass series of 2 integer tuples, which is X and Y coordinates
pygame.draw.polygon(screen,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))

# draw line need 2 point (use 2 tuples, give X and Y coordinates).
# also can specify the width of line. here we draw 2 lines in width 4.
# the other one not speficy will be defaul 1.
pygame.draw.line(screen,BLUE,(60,60),(120,60),4)
pygame.draw.line(screen,BLUE,(120,60),(60,120))
pygame.draw.line(screen,BLUE,(60,120),(120,120),4)

# draw circle takes the center and radius. the last value is width.
# if give width 0 it will means fill the whole circle.
pygame.draw.circle(screen,BLUE,(300,50),20,0)

# the 4 integers tuple gives the rectangle which exactly contains the ellipse
# [left, top, width, height].
# last parameter is width.
pygame.draw.ellipse(screen,RED,(300,250,40,80),1)


# pygame font module deals with showing words.
# Different fonts will show the letters, symblos, in different syle.
# the SysFont function call will return a Font object.
# Here we did not specify the font name(first parameter), so it will use defaul font of system.
fonBasic=pygame.font.SysFont(None,48)

# Font object has a function render(), it will return a Surface object,
# which draw letters and symbols as required.
# the surText object after call will have drawing of 'Hello World!' string letters.
# the second parameter we give the render() is True, which means draw the letters and symbols 'anti-aliased'
surText = fonBasic.render('Hello World!',True,WHITE,BLUE)
# Get the rectangle of surText, then re-position it in the center of our main window.
rectText=surText.get_rect()
rectText.centerx = screen.get_rect().centerx
rectText.centery = screen.get_rect().centery

# draw a rectangle, if not specify any value for width, defaul will be filled.
# if specify a width value, will draw rectangle with line using the width value.
pygame.draw.rect(screen,RED,(rectText.left-20,rectText.top-20,rectText.width+40,rectText.height+40))


# PixelArray is a copy of all pixels of the Surface.
# after a PixelArray was created for a Surface, the Surface will be locked and cannot draw on Surface.
# we must del the PixelArray object then can draw on Surface again.
# here we set one pixel to BLACK color. and then delete the PixelArray object.
pixArrayRoot = pygame.PixelArray(screen)
pixArrayRoot [480][380]=BLACK
del pixArrayRoot

# the blit function will draw the content of another Surface (surText) on the calling Surface (surRoot)
# the second parameter is a rectangle object. it is the place holder for the drawing.
screen.blit(surText,rectText)

# all the drawing will be on the Surface object but it will not be shown on screen.
# until we call display moduel update(), all the current things of the Surface will be shown on screen.
pygame.display.update()

# this is the main game loop, which will wait for any events (like key press, mouse click, etc.)
# and should have the code to process when certain events happened.
# Here we have the process for one event type, which is QUIT. it will be generated when mouse click
# on the top right corner "X" sign. or Windows terminate the program.
# call to pygame quit() and python sys exit() to end the program.
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


