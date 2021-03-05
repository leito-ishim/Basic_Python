class WarehouseEquipment:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extraxt(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class OfficeEquipment:
    name: str
    model: str
    manufacturer: str

    def __init__(self, model, manufacturer, name):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer

    def __str__(self):
        return f"{self.name.title() } { self.manufacturer } { self.model}"

    def __repr__(self):
        return f'{self.model} {self.manufacturer}'


class Printer(OfficeEquipment):
    type_color: str
    speed_print: float
    format_print: str

    def __init__(self, model, manufacturer, type_color, speed_print, format_print):
        super().__init__(model, manufacturer, name='Printer')
        self.type_color = "Цветной" if type_color == 1 else "Черно-белый"
        self.speed_print = speed_print
        self.format_print = format_print

    def __repr__(self):
        return f'{self.model} {self.manufacturer} {[self.type_color, "скорость печати " + str(self.speed_print) + " л/мин", "формат печати "+self.format_print]}'

    @staticmethod
    def action():
        return 'Печатает'


class Scanner(OfficeEquipment):

    speed_scan: float
    format_scan: str

    def __init__(self, model, manufacturer, speed_scan, format_scan):
        super().__init__(model, manufacturer, name='Scanner')
        self.speed_scan = speed_scan
        self.format_scan = format_scan

    @staticmethod
    def action():
        return 'Сканирует'


class Xerox(OfficeEquipment):

    type_color: bool
    speed_copy: float
    format_copy: str

    def __init__(self, model, manufacturer, type_color, speed_copy, format_copy):
        super(Xerox, self).__init__(model, manufacturer, name='Xerox')
        self.type_color = type_color
        self.speed_copy = speed_copy
        self.format_copy = format_copy

    @staticmethod
    def action():
        return 'Копирует'


a = Printer("TF01", "HP", 1, 5, "A4")
b = Printer('MA20', 'Samsung', 0, 6, "A4")
c = Xerox("FC12", "Samsung", 0, 6, "A3")
d = Scanner("XC102", "HP", 4, "A4")
e = Scanner('XC103', 'HP', 7, 'A3')


for i in a, b, c, d, e:
    print(i)


sklad = WarehouseEquipment()

sklad.add_to(a)
sklad.add_to(b)
sklad.add_to(c)
sklad.add_to(d)

print(sklad._dict)

sklad.extraxt('Scanner')


print(sklad._dict)
