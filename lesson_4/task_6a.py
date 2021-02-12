from sys import argv
from itertools import count

script_name, start_num, end_num = argv

try:
    if float(start_num) > float(end_num):
        raise Exception
    for el in count(float(start_num)):
        if el > float(end_num):
            break
        else:
            print(el)
except Exception:
    print("Второе число должно быть больше первого")
except ValueError:
    print("Последние два параметра должны быть числами")

