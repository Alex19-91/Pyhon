def two_b(a,b,c):
    my_list=[]
    my_list=[a,b,c]
    my_list.remove(min(my_list))
    my_list = sum(my_list)
    return my_list

print(two_b(a=int(input("Введите первое число:")),b=int(input("Введите второе число:")),c=int(input("Введите третье число:"))))
