import re
dict = {}
with open('5.6.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        arr = line.split(': ')
        sum = 0
        for num in re.findall('\d+', arr[1]):
            sum += int(num)

        dict[arr[0]] = sum

print(dict)
