from colorama import Fore
import time

class TrafficLight:

    __color = ""

    def running(self):
        possition = 0

        while True:
            if possition == 0:
                print(Fore.RED + "Красный")
                time.sleep(7)
                possition = 1
            if possition == 1:
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
                possition = 2
            if possition == 2:
                print(Fore.GREEN + "Зеленый")
                time.sleep(5)
                possition = 4
            if possition == 4:
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
                possition = 0


a = TrafficLight()
a.running()




