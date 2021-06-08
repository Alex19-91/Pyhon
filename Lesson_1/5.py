money_pos = int (input ("Введите размер выручки фирмы:"))
money_ng = int (input ("Введите рамер издержек фирмы:"))
if money_pos == money_ng:
    print ("Фирма работает ""в ноль")
elif (money_ng > money_pos):
        print ("Фирма работает в убыток")
elif money_pos > money_ng:
            rent = (money_pos - money_ng)/ money_pos
            chisl = int(input ("Введите количество сотрудников:"))
            rent_by_one = (money_pos-money_ng)/chisl
            print ("Фирма в плюсе, рентабельность:", rent, ",прибыль на одного сотрудника составляет:", rent_by_one)