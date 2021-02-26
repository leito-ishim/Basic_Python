class Coat:
    def __init__(self, size):
        self.consumption = float(size) / 6.5 + 0.5


class Costume:
    def __init__(self, height):
        self.consumption = 2 * float(height) +0.3


class Dress:
    def __init__(self, dress):
        self.dress = dress
        self.total_con = 0

    @property


    def dress(self):
        return self.__dress

    @dress.setter
    def dress(self, dress):
        if dress.lower() == "coat":
            self.__dress = Coat()
        elif dress.lower() == "costume":
            self.__dress = Costume()
        else:
            print("Неверный тип одежды (coat или costume")