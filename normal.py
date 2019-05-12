def big_round(num):
    if num > 0:
        return int(num) + 1
    elif num == 0:
        return num


names = ['Иван', 'Марья', 'Александр', 'Михаил', 'Вячеслав']
salaries = [100, 200, 300, 400, 1000]

obj = zip(names, salaries)
right_offset = len(max(names, key=len)) + 2


with open('salary.txt', 'w') as file:
    b = ''
    # запись в файл
    for i, j in obj:
        j = str(j)
        a = right_offset - len(i)

        for k in range( int(big_round(a / 2)) ):
            b += ' -'
        if not a % 2 == 0:
            b += ' '

        file.write(f'{i}{b} {j}\n')
        b = ''


with open('salary.txt', 'r') as file:
    res = ''
    names = []
    salaries = []
    lines = file.readlines()

    # чтение имен
    for line in lines:
        for i in line:
            if i == ' ':
                break
            res += str(i)
        names.append(res.upper())
        res = ''

    # чтение зарплат
    for line in lines:
        for i in reversed(line.strip()):
            if i == ' ':
                break
            res += str(i)
        salary = int(res[::-1])
        salaries.append( salary - salary * 0.13 )
        res = ''


# вывод в терминал
for i, j in zip(names, salaries):
    j = str(j)
    a = right_offset - len(i)

    for k in range( int(big_round(a / 2)) ):
        b += ' -'
    if not a % 2 == 0:
        b += ' '

    print(f'{i}{b} {j}')
    b = ''
