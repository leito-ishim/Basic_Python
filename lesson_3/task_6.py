def int_func(word_1):
    while True:
        flag = False
        temp = list(word_1)
        for i in temp:
            if ord(i) < 97 or ord(i) > 122:
                flag = True
        if flag == True:
            return print("Слово должно состоять только из латинских маленьких букв")
        else:
            temp[0] = chr(ord(temp[0]) - 32)
            return "".join(temp)

temp = []

my_str = input("Введите строку из слов, разделенных пробелом. Каждое слово должно состоять из латинских "
               "букв в нижнем регистре: ")

for i in my_str.split():
    temp.append(int_func(i))

try:
    print(" ".join(temp))
except TypeError:
    print("При вводе строке не соблюдено условие задачи!")


# Можно было просто воспользоваться функцией .title()

print("my name in nikita".title())

