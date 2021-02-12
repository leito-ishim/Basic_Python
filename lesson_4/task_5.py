from functools import reduce

def reducer_func(el_prev, el):
    return el_prev * el


print(reduce(reducer_func, [el for el in range(100, 1001) if el % 2 == 0]))
