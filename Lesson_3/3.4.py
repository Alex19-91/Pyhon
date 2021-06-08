def y_x(x,y):
    res=x
    if y==-1:
        res=1/res
    else:
        i=2
        while i<= abs(y):
            res*=x
            i+=1

        res=1/res
    return res
print(y_x(x=int(input("Введите целое положительное число:")),y=int(input("Введите целое отрицательное число:"))))