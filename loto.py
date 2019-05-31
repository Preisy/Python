import random


class Game:
    def __init__(self):
        self.field_user = Fields('------ Ваша карточка -----')
        self.field_computer = Fields('-- Карточка компьютера ---')
        self.game_status = True
        arr = list(set(matrix_to_list(self.field_user.field) + matrix_to_list(self.field_computer.field)))
        arr = list(filter(lambda x: not x == '', arr))
        self.start_game(arr)

    def start_game(self, numbers):
        k = len( list(filter(lambda x: not x == '', set(matrix_to_list(self.field_user.field)))) )

        while self.game_status and k > 0:
            num = random.choice(numbers)
            print(f'Новый бочонок: {num} (При отсеивании неиспользуемых в игре осталось {len(numbers) - 1})')
            self.field_user.print()
            self.field_computer.print()
            answer = input('Зачеркнуть цифру? (y/n): ')

            i, j = self.field_user.find(num)
            if answer == 'y':
                if i != 'none':
                    self.field_user.field[i][j] = ' -'
                    k -= 1
                    print()
                    i, j = self.field_user.find(num)
                    while i != 'none':
                        self.field_user.field[i][j] = ' -'
                        i, j = self.field_user.find(num)
                else:
                    self.game_status = False
                    break

            elif answer == 'n':
                if i != 'none':
                    self.game_status = False
                    break
                else:
                    print()

            else:
                print('Ответ сочтен за неправильный')
                self.game_status = False
                break

            numbers.pop(numbers.index(num))

        if self.game_status:
            print('\nВы выиграли!')
        else:
            print('\nВы проиграли!')


class Fields:
    def __init__(self, text_message):
        field = [[], [], []]
        for item in field:
            prev = 1
            i = 0
            j = 0
            while i < 9:
                if 9 - i == 5 - j:
                    while i < 9:
                        item.append(random.randint(prev, 90))
                        prev = item[-1]
                        i += 1
                        j += 1
                    break
                if random.randint(0, 1) == 1 and j < 5:
                    item.append(random.randint(prev, 90))
                    prev = item[-1]
                    i += 1
                    j += 1
                else:
                    item.append('')
                    i += 1
                    continue

        self.text_message = text_message
        self.field = field

    def print(self):
        print(self.text_message)
        for item in self.field:
            line = ''
            for i in item:
                if i == '':
                    line += '   '
                elif type(i) == type(2) and i < 10:
                    line += f' {i} '
                else:
                    line += f'{i} '
            print(line)

        print('--------------------------')

    def find(self, el):
        i = 0
        while i < len(self.field):
            j = 0
            while j < len(self.field[i]):
                if self.field[i][j] == el:
                    return i, j
                j += 1
            i += 1
        return 'none', 'none'


def matrix_to_list(matrix):
    res = []
    for line in matrix:
        for i in line:
            res.append(i)
    return res


game1 = Game()
