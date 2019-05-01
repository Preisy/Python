# Задание-1

# str = 'y = -12x + 11111140.2121'
# x = 2.5
#
# str = str[str.find('=') + 1:]
# arr = str.split()
#
# num = int(arr[0][0:-1])
# num = num * x
#
# num2 = float(arr[-1])
#
# if arr[1] == '+':
#     res = num + num2
# elif arr[1] == '-':
#     res = num - num2
#
# print(res)


# Задание-2

state = True
date = '01.11.1985'
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

# date = date.split('.')
# #Проверка лишних точек
# if len(date) > 3:
#     state = False
#
# # проверка на положительность и на отсутствие дробной части
# for i in date:
#     if int(i) < 0 and int(i) == float(i):
#         state = False
#         break
#
# # проверка на кол-во символов в частях
# if not len(date[0]) == 2 and not len(date[1]) == 2 and not len(date[2]) == 4:
#     state = False
#
# # провекра на месяц
# if int(date[1]) > 12:
#     state = False
#
# # провекра на день
# if int(date[0]) < 10 and not date[0][0] == '0':
#     state = False
# elif (int(date[1]) % 2 == 0 and int(date[0]) > 30) or (int(date[1]) % 2 == 0 and int(date[0]) > 31):
#     state = False
#
# # Проверка на год
# # Проверка на год
# if int(date[2]) < 1 or int(date[2]) > 9999 or not len(str(date[2])) == int( len( str( int(date[2]) ) ) ):
#     state = False
#
# print(state)

# Задание-3

#выводит условие в упрощенной форме. написал для понимания алгоритма
n = 14
i = 1
iprev = 0
while n > 0:
    iprev += 1
    for j in range(iprev):
        for k in range(iprev):
            print(f'{iprev}: {i}')
            n -= 1
            i += 1


flat = 0
floor = 0
previous = 0
n = 11
i = 1

while not n == i:
    previous += 1
    for j in range(previous):
        floor += 1
        flat = 1
        for k in range(previous):
            i += 1
            flat += 1
            if i == n:
                break
        if i == n:
            break

print(floor, flat)
