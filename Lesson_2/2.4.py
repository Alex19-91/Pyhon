new_str = (input('Введите несколько слов через пробел:')).split()
i=0
while i<len(new_str):
   print(i + 1,new_str[i][:10])
   i += 1
