
import random
import turtle
import time


win = turtle.Screen()
win.setup(width=600,height=600)
win.title('Snake Game')
win.bgcolor('light green')


head = turtle.Turtle()
head.shape('square')
head.color('light green','blue')
head.shapesize(1,1,2)
head.penup()
head.setheading(90)

food = turtle.Turtle()
food.shape('circle')
food.color('black','red')
food.shapesize(0.5,0.5)
food.penup()
food.setpos(0,100)

tail = turtle.Turtle()
tail.shape('square')
tail.color('light green','light blue')
tail.shapesize(1,1,2)
tail.penup()
tail.setpos(-20,0)
tail.stamp()

wiper = turtle.Turtle()
wiper.shape('square')
wiper.color('light green','light green')
wiper.shapesize(1,1,2)
wiper.penup()
wiper.setpos(-40,0)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.setpos(0, 250)
pen.write('Score : 0  High Score : 0', align='center',
          font=('Times New Roman', 24, 'bold'))


score = 0
high_score = 0
delay = 0.1
game_start = False
game_exit = False
length = 1
tail_pos = [(-20,0)]


'''
>  0
^  90
<  180
v  270
'''
# assigning key directions
def gonorth():
    if not game_start:
        return
    if head.heading() != 270:
        head.setheading(90)
  
def gosouth():
    if not game_start:
        return
    if head.heading() != 90:
        head.setheading(270)
  
def gowest():
    if not game_start:
        return
    if head.heading() != 0:
        head.setheading(180)
  
def goeast():
    if not game_start:
        return
    if head.heading() != 180:
        head.setheading(0)
  
  
def head_move():
    pos = head.pos()
    head.forward(20)
    return(pos)

def start_pause():
    global game_start
    game_start = not game_start

def exit_game():
    global game_exit
    game_exit = True


win.onkeypress(gonorth, 'w')
win.onkeypress(gonorth, 'Up')
win.onkeypress(gosouth, 's')
win.onkeypress(gosouth, 'Down')
win.onkeypress(gowest, 'a')
win.onkeypress(gowest, 'Left')
win.onkeypress(goeast, 'd')
win.onkeypress(goeast, 'Right')
win.onkeypress(start_pause, 'space')
win.onkeypress(exit_game, 'x')
win.listen()
win.tracer(0)


def gameover():
    global game_start
    global score
    global high_score
    global delay
    global length
    time.sleep(1)
    game_start = False
    head.setpos(0, 0)
    head.setheading(90)
    if score > high_score:
        high_score = score
    score = 0
    while len(tail_pos)>0:
        wiper.setpos(tail_pos.pop(0))
        wiper.stamp()
    tail.setpos(-20,0)
    length = 1
    tail_pos.append((-20,0))
    tail.stamp()
    pen.clear()
    pen.write('Score : {} High Score : {} '.format(score, high_score),
              align='center', font=('Times New Roman', 24, 'bold'))

# Main Gameplay
while not game_exit:

    win.update()

    if not game_start:
        time.sleep(delay)
        continue

    pos = head_move()
    tail_pos.append(pos)
    tail.setpos(pos)
    tail.stamp()
    
    x,y = head.pos()
    # collision with wall
    if x > 290 or x < -290 or y > 290 or y < -290:
        gameover()
    
    # collision with tail
    for pos in tail_pos:
        if head.distance(pos) < 19:
            gameover()
    
    # eat food
    if head.distance(food) < 15:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.setpos(x, y)
        length+=1
        score+=10
        pen.clear()
        pen.write('Score : {} High Score : {} '.format(score, high_score),
                  align='center', font=('Times New Roman', 24, 'bold'))

    while len(tail_pos)>length:
        wiper.setpos(tail_pos.pop(0))
        wiper.stamp()

    time.sleep(delay)

pen.color('red')
pen.clear()
pen.write('Game Over', align='center', font=('Times New Roman', 24, 'bold'))
win.mainloop()




'''
Name                       Red  Green  Blue
antique white              250   235   215
aquamarine                 127   255   212
azure                      240   255   255
black                        0     0     0
blue                         0     0   255
blue violet                138    43   226
brown                      165    42    42
chocolate                  210   105    30
coral                      255   127    80
cyan                         0   255   255
dark blue                    0     0   139
dark cyan                    0   139   139
dark green                   0   100     0
dark grey                  169   169   169
dark magenta               139     0   139
dark orange                255   140     0
dark red                   139     0     0
dark salmon                233   150   122
dark violet                148     0   211
deep pink                  255    20   147
deep sky blue                0   191   255
dim grey                   105   105   105
firebrick                  178    34    34
floral white               255   250   240
forest green                34   139    34
ghost white                248   248   255
gold                       255   215     0
green                        0   255     0
green yellow               173   255    47
grey                       190   190   190
honeydew                   240   255   240
hot pink                   255   105   180
indian red                 205    92    92
ivory                      255   255   240
khaki                      240   230   140
lavender                   230   230   250
lawn green                 124   252     0
light blue                 173   216   230
light coral                240   128   128
light cyan                 224   255   255
light goldenrod            238   221   130
light green                144   238   144
light grey                 211   211   211
light pink                 255   182   193
light salmon               255   160   122
light yellow               255   255   224
lime green                  50   205    50
linen                      250   240   230
magenta                    255     0   255
medium blue                  0     0   205
medium orchid              186    85   211
medium purple              147   112   219
midnight blue               25    25   112
misty rose                 255   228   225
moccasin                   255   228   181
navy blue                    0     0   128
orange                     255   165     0
orange red                 255    69     0
orchid                     218   112   214
pink                       255   192   203
plum                       221   160   221
purple                     160    32   240
red                        255     0     0
rosy brown                 188   143   143
royal blue                  65   105   225
saddle brown               139    69    19
salmon                     250   128   114
sandy brown                244   164    96
sea green                   46   139    87
sky blue                   135   206   235
snow                       255   250   250
spring green                 0   255   127
tomato                     255    99    71 
turquoise                   64   224   208
violet                     238   130   238
wheat                      245   222   179
white                      255   255   255
yellow                     255   255     0
yellow green               154   205    50
'''
