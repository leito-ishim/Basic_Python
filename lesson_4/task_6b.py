from sys import argv
from itertools import cycle

script_name, num_rereat = argv

c = 1
for el in cycle("OK!"):
    if c > int(num_rereat):
        break
    print(el)
    c += 1
