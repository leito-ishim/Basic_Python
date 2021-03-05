from datetime import datetime


class Date:

    @classmethod
    def date_for_int(cls, date):
        #Вариант преобразования без использования модуля datetime
        #day = int(date[:date.index("-"):])
        #month = int(date[date.index("-")+1:date.index("-", date.index("-")+1):])
        #year = int(date[date.index("-", date.index("-")+1)+1::])

        my_date = datetime.strptime(date, "%d-%m-%Y")
        return print(f"Число: {my_date.day}, тип даннных {type(my_date.day)}\n"
                     f"Месяц: {my_date.month}, тип даннных {type(my_date.month)}\n"
                     f"Год: {my_date.year}, тип даннных {type(my_date.year)}\n")

    @staticmethod
    def validation_date(date):
        try:
            return print(datetime.strptime(date, "%d-%m-%Y").date())
        except ValueError:
            print("Неверный формат даты либо такой даты не существует. Формат даты для ввода: dd-mm-yyyy")


Date.date_for_int("29-02-2016")
Date.validation_date("29-02-2020")
Date.validation_date("29-02-2017")

