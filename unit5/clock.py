
import turtle
import datetime

clock_radius = 160

def move(t, distance):
    t.penup()
    t.forward(distance)
    t.pendown()

def createHand(win, name, length):
    t = turtle.Pen()
    t.hideturtle()
    move(t, -10)
    t.begin_poly()
    t.forward(length + 10)
    t.end_poly()
    hand = t.get_poly()
    win.register_shape(name, hand)
    t.clear()
    del t

def createClock(radius):
    t = turtle.Pen()
    t.hideturtle()
    t.pensize(7)
    for i in range(60):
        move(t, radius)
        if i % 5 == 0:
            t.forward(20)
            move(t, -radius-20)
        else:
            t.dot(5)
            move(t, -radius)
        t.right(6)
    t.penup()
    # write clock numbers
    t.home()
    t.forward(clock_radius-30)
    t.write('12', align='center', font=('Courier', 14, 'bold'))
    t.home()
    t.back(clock_radius-5)
    t.write('6', align='center', font=('Courier', 14, 'bold'))
    t.home()
    t.right(95)
    t.forward(clock_radius-15)
    t.write('3', align='center', font=('Courier', 14, 'bold'))
    t.home()
    t.left(95)
    t.forward(clock_radius-15)
    t.write('9', align='center', font=('Courier', 14, 'bold'))
    t.home()
    del t

'''weekdays'''
def getWeekday(today):
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][today.weekday()]

'''date'''
def getDate(today):
    return f'{today.day} / {today.month} / {today.year}'

def startTick(win, second_hand, minute_hand, hour_hand, printer):
    today = datetime.datetime.today()
    second = today.second + today.microsecond * 1e-6
    minute = today.minute + second / 60.
    hour = (today.hour + minute / 60) % 12
    # heading
    second_hand.setheading(6 * second)
    minute_hand.setheading(6 * minute)
    hour_hand.setheading(30 * hour)

    printer.forward(clock_radius/3)
    printer.write(getWeekday(today), align='center', font=('Courier', 14, 'bold'))
    printer.home()
    printer.back(clock_radius/2)
    printer.write(getDate(today), align='center', font=('Courier', 14, 'bold'))
    printer.home()
    # 100ms to tick once
    win.ontimer(lambda :startTick(win, second_hand, minute_hand, hour_hand, printer), 100)


def start(win):
    # stop update graph
    win.tracer(False)
    win.mode('logo')
    createHand(win, 'second_hand', clock_radius-10)
    createHand(win, 'minute_hand', clock_radius-40)
    createHand(win, 'hour_hand', clock_radius-80)
    # turtle using the shape created
    second_hand = turtle.Turtle()
    second_hand.shape('second_hand')
    minute_hand = turtle.Turtle()
    minute_hand.shape('minute_hand')
    hour_hand = turtle.Turtle()
    hour_hand.shape('hour_hand')
    for hand in [second_hand, minute_hand, hour_hand]:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    # printer for write dynamic information (weekday, date)
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()

    createClock(clock_radius)
    # start update graph
    win.tracer(True)
    win.ontimer(lambda :startTick(win, second_hand, minute_hand, hour_hand, printer), 100)
    win.mainloop()


if __name__ == '__main__':
    wn = turtle.Screen()
    wn.title('Clock by Turtle')
    wn.bgcolor('light green')
    start(wn)
