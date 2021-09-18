import turtle


s=turtle.Screen()
t=turtle.Pen()
t.penup()

s.title('draw snowflake')
s.setup(1024,768)

t.goto(0,320)
t.setheading(300)
t.speed(0)

t.pendown()


def draw_cuspline5():
    t.fd(1)
    t.lt(60)
    t.fd(1)
    t.rt(120)
    t.fd(1)
    t.lt(60)
    t.fd(1)

def draw_cuspline4():
    draw_cuspline5()
    t.lt(60)
    draw_cuspline5()
    t.rt(120)
    draw_cuspline5()
    t.lt(60)
    draw_cuspline5()

def draw_cuspline3():
    draw_cuspline4()
    t.lt(60)
    draw_cuspline4()
    t.rt(120)
    draw_cuspline4()
    t.lt(60)
    draw_cuspline4()

def draw_cuspline2():
    draw_cuspline3()
    t.lt(60)
    draw_cuspline3()
    t.rt(120)
    draw_cuspline3()
    t.lt(60)
    draw_cuspline3()

def draw_cuspline1():
    draw_cuspline2()
    t.lt(60)
    draw_cuspline2()
    t.rt(120)
    draw_cuspline2()
    t.lt(60)
    draw_cuspline2()

def draw_cuspline(steps):
    if steps<3:
        t.fd(steps)
        t.lt(60)
        t.fd(steps)
        t.rt(120)
        t.fd(steps)
        t.lt(60)
        t.fd(steps)
    else:
        steps=steps/3
        draw_cuspline(steps)
        t.lt(60)
        draw_cuspline(steps)
        t.rt(120)
        draw_cuspline(steps)
        t.lt(60)
        draw_cuspline(steps)

for i in range(3):
    draw_cuspline(81)
    t.rt(120)

s.mainloop()