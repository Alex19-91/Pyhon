dict_1= {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}
result = []
with open("str_5.4.txt",  "r", encoding="utf-8") as file:
    file_lines = file.readlines()
    separator = ' — '
    for str in file_lines:
        arr = str.split(separator)
        result.append(dict_1.get(arr[0]) + separator + arr[1])
with open('str_5.4_result.txt', 'w', encoding='utf-8') as result_file:
    result_file.writelines(result)
print(result)