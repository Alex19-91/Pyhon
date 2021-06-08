month_dictionary = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer',
                    8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
month = int(input('Введите номер месяца (от 1 до 12):'))
if month <= 12 & month >= 1:
    print(month_dictionary.get(month))
else:
    print('Ошибка!')