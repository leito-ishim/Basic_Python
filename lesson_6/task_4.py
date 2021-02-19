class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала!")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч")


class PoliceCar(Car):
    pass


audi = SportCar(150, "Red", "RS8", False)
audi.go()

toyota = TownCar(80, "Black", "Corolla", False)
toyota.show_speed()
toyota.turn("Налево")

yaz = WorkCar(50, "White", "Уаз Патриот", False)
yaz.show_speed()

