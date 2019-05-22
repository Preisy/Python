# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:
    def __init__(self, name, color, type_toy):
        self.type_toy = self.whichType(name, color, type_toy)

    def whichType(self, name, color, type_toy):
        if type_toy == 'Животное':
            return Animal(name, color)
        elif type_toy == 'Персонаж мультфильма':
            return CartoonCharacter(name, color)

    def startMaking(self, name, color, type_toy):
        self.rawMaterial(color, type_toy)
        self.sewing(type_toy)
        self.coloring(color)

    def rawMaterial(self, color, type_toy):
        print(f'Закупка сырья. Тип игрушки: {type_toy}, цвет: {color}')

    def sewing(self, type_toy):
        print(f'Пошив. Тип игрушки: {type_toy}')

    def coloring(self, color):
        print(f'Окраска игрушки. Цвет: {color}')

class Animal(Toy):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.startMaking(name, color, 'Животное')

class CartoonCharacter(Toy):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.startMaking(name, color, 'Персонаж мультфильма')


toy = Toy('Миша', 'Красный', 'Персонаж мультфильма').type_toy
print(toy.color, toy.name)

