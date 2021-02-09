def user_info(**kwargs):
    return kwargs


user = user_info(name="Никита", surname="Козлов", year_birth=1989, city="Нефтекамск", mail="test@mail.ru",
                 phone="89177777777")

print(f"Пользователя зовут {user.get('name')} {user.get('surname')}.\nРодился в {user.get('year_birth')} году.\n"
      f"Проживает в городе {user.get('city')}.\nКонтактные данные:\n\te-mail: {user.get('mail')}\n\t"
      f"телефон: {user.get('phone')}")

