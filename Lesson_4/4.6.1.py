from sys import argv
name, beg, end_ = argv
from itertools import count
print(name)
for el in count(int(beg)):
    if el > int(end_):
        break
    else:
        print(el)