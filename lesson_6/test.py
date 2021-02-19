import turtle
import time


def print_trafficlight(color_1, color_2, color_3, pause):

    turtle.color(color_1)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()

    turtle.color(color_2)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()

    turtle.color(color_3)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    time.sleep(pause)

    turtle.clear()

    turtle.done()


print_trafficlight("black", "yellow", "black", 2)





