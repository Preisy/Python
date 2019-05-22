# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os

# Задача-1:
if __name__ == '__main__':
    for i in range(1, 10):
        os.mkdir(f'dir_{i}')

    for i in range(1, 10):
        os.rmdir(f'dir_{i}')


# Задача-2:
# if __name__ == '__main__':
#     a = os.listdir().copy()
#     print([i for i in os.listdir().copy() if os.path.isdir(i)])

# Задача-3:
# if __name__ == '__main__':
#     from shutil import copyfile
#
#     copyfile('easy.py', 'easy_01.py')

# Функции
def changeDir(path):
    os.chdir(f'{os.getcwd()}\{path}')
