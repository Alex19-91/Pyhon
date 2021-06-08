from sys import argv
a_1, a_2, a_3,a_4 = argv
print("Название программы: ", a_1)
print("Ставка: ", a_2)
print("Количество часов: ", a_3)
print("Премия: ", a_4)
print('Зарплата =',int(a_2)*int(a_3) +int(a_4))