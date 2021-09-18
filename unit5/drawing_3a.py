

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

for i in range(200):
    t.pen(pencolor=colors[i%4])
    t.forward(i)
    t.left(92)


turtle.done()
#s.mainloop()
