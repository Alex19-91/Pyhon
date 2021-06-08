orig_list = [1,2,2,3,4,4,5,6,6,7,8,8,9]
new_list = [el for el in orig_list if orig_list.count(el)==1]
print (new_list)