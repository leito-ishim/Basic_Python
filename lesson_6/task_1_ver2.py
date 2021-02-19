from colorama import Fore
import time

class TrafficLight:

    __color = ""

    def running(self):
        delta = 1
        color_list = ["красный", "желтый", "зеленый"]
        pause_list = [7, 2, 5]
        color_font_list = [Fore.RED, Fore.YELLOW, Fore.GREEN]
        start_color = input("С какого цвета начать?")
        start_position = color_list.index(start_color.lower())
        while True:
            print(color_font_list[start_position] + color_list[start_position].title())
            time.sleep(pause_list[start_position])

            if start_position == 0:
                delta = 1
            elif start_position >= 2:
                delta = -1
            start_position += delta


a = TrafficLight()
a.running()