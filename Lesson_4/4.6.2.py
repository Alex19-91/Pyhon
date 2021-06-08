from sys import argv
name, beg_1, end_2 = argv
from itertools import cycle
my_list=list('1234567890')
c = int(beg_1)
for el in cycle(my_list):
    if c > int(end_2):
        break
    print(el)
    c += 1
