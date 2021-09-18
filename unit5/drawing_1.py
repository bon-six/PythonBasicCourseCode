

import turtle


t = turtle.Pen()
s = turtle.Screen()

s.title('My Turtle Drawing')
s.bgcolor('white')

t.shape('classic')
t.shapesize(1,1,1)


t.pen(pencolor='red',fillcolor='green',pensize=3,speed=5)

t.begin_fill()

for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()

t.goto(100,100)
t.pendown()
t.circle(60)

t.end_fill()

turtle.done()
#s.mainloop()
