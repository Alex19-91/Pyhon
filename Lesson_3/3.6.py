def int_func():
    str_1 = input('Введите слова маленькими латинскими буквами:').split()
    for word in str_1:
        per_1=0
        for sym in word:
            if 97<= ord(sym) <=122:
                per_1+=1
        if per_1==len(word):
            print(word.title())
        else:
            print('Вводите только маленькие буквы на латинице.')




int_func() 
