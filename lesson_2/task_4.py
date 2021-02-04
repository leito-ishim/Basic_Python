my_str = input("Введите несколько слов, разделенных пробелами: ")

for ind, el in enumerate(my_str.split()):
    print(ind, el[0:10])



