i=0
my_list=[]
newlist_1=[]
newlist_2=[]
newlist_3=[]
newlist_4=[]
name ={}
price={}
num={}
iz={}
new_dict={}
while i<4:
    my_dict = {'название': input('Введите название  товара:'), 'цена': input('Введите цену  товара:'),
               'количество': input('Введите количество товара:'), 'единица': input('Введите единицу измерения:')}
    my_tuple = i+1, my_dict
    my_list.append(my_tuple)
    name=my_dict.get('название')
    price=my_dict.get('цена')
    num=my_dict.get('количество')
    iz=my_dict.get('единица')
    newlist_1.append(name)
    newlist_2.append(price)
    newlist_3.append(num)
    newlist_4.append(iz)
    i+=1
new_dict= {'название':newlist_1, 'цена': newlist_2, 'количество': newlist_3, 'единица': newlist_4}
print(new_dict)
