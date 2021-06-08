my_list = [7, 6 ,5, 4, 4, 3, 2]
new = int(input('Введите число:'))
i=-1
while new > my_list[i]:
    i-=1
my_list.insert(i+1, new)
print(my_list)