# import required modules
import turtle
import random
import math
  
# Creating a window screen
wn = turtle.Screen()
wn.title("Treasure Find Game")
wn.bgcolor("white")
# the width and height can be put as user's choice
WIDTH=1162
HEIGHT=874
wn.setup(width=WIDTH+10, height=HEIGHT+10)

RANGE = math.sqrt(WIDTH**2+HEIGHT**2)
FIND_DISTANCE = RANGE/10

wn.bgpic('Treasure-Map2.gif')

target = (random.randint(0,WIDTH)-WIDTH//2, random.randint(0,HEIGHT)-HEIGHT//2)

printer = turtle.Turtle()
printer.hideturtle()
printer.penup()

def remove_write():
    printer.clear()
    printer.home()

def on_click (x,y):

    distance = math.sqrt((x-target[0])**2 + (y-target[1])**2)

    if (distance < FIND_DISTANCE):
        hint = "You find it!"
    elif (distance < FIND_DISTANCE*2):
        hint = "Boiling hot!"
    elif (distance < FIND_DISTANCE*3):
        hint = "Really hot"
    elif (distance < FIND_DISTANCE*4):
        hint = "Hot";
    elif (distance < FIND_DISTANCE*5):
        hint = "Warm"
    elif (distance < FIND_DISTANCE*6):
        hint = "Cold"
    elif (distance < FIND_DISTANCE*7):
        hint = "Really cold";
    else:
        hint = "Freezing!";

    printer.goto(x,y)
    printer.write(hint, align='center', font=('Courier', 14, 'bold'))

    if hint=='You find it!':
        wn.onclick(None)
    else:
        turtle.ontimer(remove_write, 500)

wn.onclick(on_click)
  
wn.mainloop()
