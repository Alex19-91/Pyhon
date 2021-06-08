my_list = [1,2,3,4,4,5,4,5,6,7,6,8]
new_list = [my_list[num] for num in range(1,len(my_list)) if my_list[num]>my_list[num-1]]
print(new_list)
