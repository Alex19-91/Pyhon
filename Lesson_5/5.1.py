#from math import inf
str_1 = open("str_1.txt", "w")
str_list = []
i = 0

while True:
    str = input('Введите что-то')
    if (str == ''):
        break

    str_list.append(str + '\n')
    i += 1

str_1.writelines(str_list)
str_1.close()
