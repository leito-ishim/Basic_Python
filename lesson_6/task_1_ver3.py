import turtle
import time


class TrafficLight:

    def running(self):
        delta = 1
        start_position = 0
        while True:
            if start_position == 0:
                self.print_traffic_light("red", "black", "black", 7)
                delta = 1
            elif start_position == 1:
                self.print_traffic_light("black", "yellow", "black", 2)
            elif start_position >= 2:
                self.print_traffic_light("black", "black", "green", 5)
                delta = -1

            start_position += delta


    def print_traffic_light(self, color_1, color_2, color_3, pause):

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


a = TrafficLight()

