def sum_str():
    sum_1 =0
    while True:
        str_1 =input ('Введите числа через пробел (для выхода введите q):').split()
        for num in str_1:
            if num=="q":
                return sum_1
            else: sum_1+=int(num)
        print('Сумма =',sum_1)



print (sum_str())