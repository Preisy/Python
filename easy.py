#
# easy Lesson_01
#

# Задача-1

a = input('Введите a: ')
b = input('Введите b: ')
c = input('Введите c: ')
d = input('Введите d: ')
print('a: ' + a + ', b: ' + b + ', c: ' + c + ', d: ' + d)

# Задача-2

a = input('Введите a: ')
a = int(a) + 2
print(a)

# Задача-3

prompt = input('Введите ваш возраст: ')
if int(prompt) >= 18:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
