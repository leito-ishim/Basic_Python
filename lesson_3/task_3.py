def my_func(num_1, num_2, num_3):

    """Функция принимпет три числа и возвращает сумму двух больших из них"""

    my_list = sorted([num_1, num_2, num_3], reverse=True)
    return my_list[0] + my_list[1]

#Та же функция но анонимная

my_func_1_line = lambda num_1, num_2, num_3: sorted([num_1, num_2, num_3], reverse=True)[1] + \
                                            sorted([num_1, num_2, num_3], reverse=True)[0]

print(my_func(10, 20, 30))
print(my_func_1_line(10, 20, 30))
