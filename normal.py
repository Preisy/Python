# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


# Я не добавлял классы Player и Enemy так как получается, что по заданию они нужны для создания всего лишь одного экземпляра
# Тогда легче и быстрее будет сделать так
# Что игрок и соперник являются лишь экзмеплярами класса Person и атриутами game_01

# На мой взгляд со словарем работать удобнее
class Person(dict):
    def __init__(self, health, damage, armor):
        self['health'] = health
        self['damage'] = damage
        self['armor'] = armor

    def attack(self, enemy):
        enemy['health'] -= self['damage']
        enemy['health'] = round(enemy['health'], 2)

    def _calculateDamage(self, enemy):
        self['damage'] = round(self['damage'] / enemy['armor'], 2)

class Game(dict):
    def __init__(self, player, enemy):
        self['player'] = player
        self['enemy'] = enemy

        self['damages'] = [self['player']['damage'], self['enemy']['damage']]
        self['player']._calculateDamage(self['enemy'])
        self['enemy']._calculateDamage(self['player'])

    def start(self):
        while self['player']['health'] >= 0 and self['enemy']['health'] >= 0:
            self['player'].attack(self['enemy'])
            self['enemy'].attack(self['player'])

        self['player']['damage'] = self['damages'][0]
        self['enemy']['damage'] = self['damages'][1]
        self.popitem()
        return self


persons = [[100, 50, 1.2], [150, 20, 1.2]]
for i, j in enumerate(persons):
    persons[i] = Person(*j)

game_01 = Game(persons[0], persons[1])
total = game_01.start()
print(total)
