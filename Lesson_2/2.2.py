my_list = input ("Введите значения элементов списка через пробел:")
my_list = my_list.split()
i = 1
a = my_list[i]
while i< len(my_list):
   a= my_list[i-1]
   my_list[i-1] = my_list[i]
   my_list[i] = a
   i+=2

print (my_list)

