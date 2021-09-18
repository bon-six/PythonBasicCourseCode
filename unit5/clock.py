
import turtle
import datetime

clock_radius = 160

def move(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()



def createHand(name, length):
    turtle.reset()
    move(-10)
    turtle.begin_poly()
    turtle.forward(length + 10)
    turtle.end_poly()
    hand = turtle.get_poly()
    turtle.register_shape(name, hand)


def createClock(radius):
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        move(radius)
        if i % 5 == 0:
            turtle.forward(20)
            move(-radius-20)
        else:
            turtle.dot(5)
            move(-radius)
        turtle.right(6)
    # write clock numbers
    turtle.home()
    turtle.penup()
    turtle.forward(clock_radius-30)
    turtle.write('12', align='center', font=('Courier', 14, 'bold'))
    turtle.home()
    turtle.back(clock_radius-5)
    turtle.write('6', align='center', font=('Courier', 14, 'bold'))
    turtle.home()
    turtle.right(95)
    turtle.forward(clock_radius-15)
    turtle.write('3', align='center', font=('Courier', 14, 'bold'))
    turtle.home()
    turtle.left(95)
    turtle.forward(clock_radius-15)
    turtle.write('9', align='center', font=('Courier', 14, 'bold'))
    turtle.home()

'''weekdays'''
def getWeekday(today):
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][today.weekday()]


'''date'''
def getDate(today):
    return f'{today.day} / {today.month} / {today.year}'



def startTick(second_hand, minute_hand, hour_hand, printer):
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
    turtle.ontimer(lambda :startTick(second_hand, minute_hand, hour_hand, printer), 100)


def start():
    # stop update graph
    turtle.tracer(False)
    turtle.mode('logo')
    createHand('second_hand', clock_radius-10)
    createHand('minute_hand', clock_radius-40)
    createHand('hour_hand', clock_radius-80)
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
    turtle.tracer(True)
    turtle.ontimer(lambda :startTick(second_hand, minute_hand, hour_hand, printer), 100)
    turtle.mainloop()


if __name__ == '__main__':
    start()
