# Задача-1:

arr = ['Яблоко', 'Абрикос', 'Авокадо', 'Вишня', 'Оливки']
str = ''
max = int(len(arr[0]))

for i in arr:
    if int(len(i)) > max:
        max = int(len(i))

j = 0
for i in arr:
    str = f'{j}. '
    for _ in range( max - int(len(i)) ):
        str += ' '
    str += i
    print(str)
    j += 1

print()

#Задача-2
list2 = []
list = [1, 2, 3, 4, 6, 7, 87, 8, 98]
list1 = [234, 21, 34, 14, 1, 2, 8]
c = (set(list) - set(list1))
for i in c:
    list2.append(i)
print(list2)

#Задача-3

arr = [2, 5, 52, 23, 6, 23, 64, 2, 7, 23, 34, 5, 2]
newArr = []
for i in arr:
    if i % 2 == 0:
        newArr.append(i / 4)
    else:
        newArr.append(i * 2)

print(arr)
print(newArr)
