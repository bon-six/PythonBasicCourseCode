
import turtle

s=turtle.Screen()
s.title('Turtle Drawing')
s.bgcolor('white')

t=turtle.Pen()

t.color('red', 'yellow')
t.speed(0)

t.begin_fill()

while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()

s.mainloop()
