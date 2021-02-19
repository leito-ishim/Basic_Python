class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass_asphalt(self, thickness):
        print(f"Для покрытия дороги длиной - {self._length} м, шириной {self._width} м, "
              f"при толщине слоя - {thickness} см., понадобится"
              f" {self._length * self._width * 25 * thickness / 1000} тонн асфальта. \nНорма асфальта для покрытия "
              f"одного кв метра дороги, толщиной в 1 см = 25 кг.")


a = Road(5000, 20)

a.calc_mass_asphalt(5)
