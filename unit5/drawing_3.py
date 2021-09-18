

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
    for j in range(3):
        t.pendown()
        t.pen(pencolor=colors[j%5])
        t.circle(int(i/5))
        t.left(120)
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.forward(i*2)
    t.left(92)


turtle.done()
#s.mainloop()
