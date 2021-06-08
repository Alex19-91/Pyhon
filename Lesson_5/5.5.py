sum = 0
with open('str_5.5.txt', 'w+', encoding='utf-8') as file:
    file.write(input('Enter your numbers by space:'))
    file.seek(0)

    for num in file.read().split():
        sum+= int(num)
print(sum)
