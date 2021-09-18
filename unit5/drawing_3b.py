

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
t.penup()

for i in range(5,120):
    t.pen(pencolor=colors[i%5])
    t.fd(3*i)
    t.write('Bob',font=('Verdana',i//5,'normal'))
    t.left(74)


turtle.done()
#s.mainloop()
