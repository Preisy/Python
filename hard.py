# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

#
# НЕ РАБОТАЕТ CD
#

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
from shutil import copyfile
import re
print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def cp():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        copyfile(dir_name, "{}_copy.{}".format(re.findall('^.+(?=\.)', dir_name)[0], re.findall('[^\.]+$', dir_name)[0]))
        print(f'Копия файла {dir_name} создана')
    except:
        print(f'Файла {dir_name} не существует')

def rm():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    answer = input('Вы точно подтверждаете удаление? y/n: ')
    if answer == 'y':
        os.remove(dir_name)
    else:
        return

def cd():
    if not dir_name:
        print("Необходимо указать путь вторым параметром")
        return
    if re.findall('^[^\/]+', dir_name)[0] in os.listdir():
        # print(os.getcwd(), dir_name)
        os.chdir(f'{os.getcwd()}/{dir_name}')
        # print(os.getcwd())
    else:
        print(dir_name)
        os.chdir(dir_name)

def ls():
    print(os.listdir())
    print(os.getcwd())

def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

