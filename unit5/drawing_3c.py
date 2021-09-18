

import turtle


t = turtle.Pen()
s = turtle.Screen()
#s = t.getscreen()

s.title('My Turtle Drawing')
s.bgcolor('black')

t.shape('classic')
t.shapesize(1,1,1)


t.pen(speed=0)


# 2 spin rosette, 4 sides

colors = ['red','green','yellow','blue','purple']

for i in range(100):
    pos = t.position()
    heading = t.heading()
    for j in range(1,i):
        t.pendown()
        t.pen(pencolor=colors[j%4])
        t.forward(j)
        t.left(92)
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.forward(i*3)
    t.left(92)


turtle.done()
#s.mainloop()
