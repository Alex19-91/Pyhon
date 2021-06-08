month = int(input('Введите номер месяца (от 1 до 12):'))
while month<1 or month>12:
    month = int (input('Введите номер месяца (от 1 до 12):'))
month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if month==month_list[0] or month==month_list[1]or month==month_list[2]:
    print('Winter')
elif month==month_list[3] or  month==month_list[4]  or month==month_list[4]:
    print('Spring')
elif month==month_list[6] or month==month_list[7] or month==month_list[8]:
    print('Summer')
else: print ('Autumn')


