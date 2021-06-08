
with open("str_2.txt",  "r", encoding="utf-8") as file:
    file_lines = file.readlines()
    average_salary=0
    print('У кого меньше 20к:')
    for str in file_lines:
        person = str.split()
        average_salary+= int(person[1])
        if int(person[1]) < 20000:
            print (person[0])
    print('\nAverage=',average_salary/len(file_lines))