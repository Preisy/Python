# Задача-1

arr = [2, -5, 8, 9, -25, 25, 4]
newArr = []

for i in arr:
    i = i ** 0.5 or False
    if not type(i) == complex and float(i) == int(i):
        newArr.append(int(i))

print(newArr)
print()

# Задача-2

date = '02.11.2013'

dot = date.find('.')
day = int(date[:dot])
date = date[dot + 1:]

dot = date.find('.')
month = int(date[:dot])
date = date[dot + 1:]

year = int(date[:])

print(f'{day} {month} {year} года')

# Задача-3

import random

n = int(input('Сколько должно быть элементов: '))
arr = []

for _ in range(n):
    arr.append(round(random.random() * 200 - 100))

print(arr)

# Задача-4

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = set(lst)
print(lst2)

index = ''
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = []
for i in lst:
    index = lst.index(i)
    elem = lst[index]
    lst[index] = False
    print(elem)
    if not i in lst:
        lst2.append(elem)
    lst[index] = elem

print(lst2)
