
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
    return pos

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
