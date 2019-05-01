#
# easy Lesson_01
#

# Задача-1

a = int(input('Введите число: '))
while not(a > 0 and a < 10):
    a = int(input('Введите число: '))

# Задача-2

a, b = int(input('Введите a: ')), int(input('Введите b: '))

a = a - b
b = a + b
a = b - a

# a, b = b, a

print('a:', a)
print('b:', b)
