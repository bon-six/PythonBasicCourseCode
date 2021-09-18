

import turtle


t = turtle.Pen()
s = t.getscreen()

s.title('My Turtle Drawing')
s.bgcolor('white')

t.shape('classic')
t.shapesize(1,1,1)

t.pen(pencolor='red',fillcolor='yellow',speed=5)

t.begin_fill()

# petal, 4

for i in range(4):
    t.circle(100,90)
    t.left(90)
    t.circle(100,90)

t.end_fill()

turtle.done()







