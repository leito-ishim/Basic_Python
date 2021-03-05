class Division:

    @classmethod
    def division(cls, a, b):
        try:
            return print(a/b)
        except ZeroDivisionError:
            print("На 0 делить нельзя")


Division.division(2, 0)
