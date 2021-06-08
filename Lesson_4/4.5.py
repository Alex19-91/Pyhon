n_list= [el for el in range(100, 1001, 2)]
print(n_list)
from functools import reduce
def new_func (prev_el,el):
    return prev_el*el

print(reduce(new_func, n_list))