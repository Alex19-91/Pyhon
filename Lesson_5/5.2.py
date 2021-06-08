file = open("str_1.txt", "r")
file_lines = file.readlines()
i = 1
print('Кол-во строк:',len(file_lines))
for str in file_lines:
    print('Кол-во слов в строке', i, ':', len(str.split()))
    i+=1
file.close()