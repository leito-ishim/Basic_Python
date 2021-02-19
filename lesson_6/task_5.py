class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки!")


class Pen(Stationery):

    def draw(self):
        print(f"Отрисовка при помощи: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Выбрана отрисовка при помощи: {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Закрашивание с помощью: {self.title}")


red_pen = Pen("Красная ручка")
red_pen.draw()

green_pensil = Pencil("Зеленый карандаш")
green_pensil.draw()

yellow_handle = Handle("Желтый маркер")
yellow_handle.draw()

