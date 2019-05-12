# Задание - 1
players = [
    {
        'name': 'qwe',
        'health': 100,
        'damage': 50,
        'armor': 1.2
    },
    {
        'name': 'ewq',
        'health': 150,
        'damage': 20,
        'armor': 1.2
    }
]


def attack(attacking, attacked):
    attacked['health'] = round(attacked['health'] - attacking['damage'], 2)

# attack(players[0], players[1])

# Задание - 2

# изменение урока игрока
def armor(p1, p2):
    p1["damage"] = round(p1["damage"] / p2["armor"], 2)
    p2["damage"] = round(p2["damage"] / p1["armor"], 2)

# запись данных игроков в файлы
for player in players:
    with open(f'{player["name"]}.txt', 'w') as file:
        file.write('{\n')
        for j in player:
            file.write(f"    '{j}': ({player[j]})\n")
        file.write('}')
players = []

# создание обьекта игрока
def render_player(name):
    user = {}
    word_status_name = False
    word_status_value = False
    str_name = ''
    str_value = ''
    with open(f'{name}.txt', 'r') as file:
        for i in file.readlines():

            for symbol in i.strip():

                if symbol == "'":
                    word_status_name = not word_status_name
                if word_status_name and not symbol == "'":
                    str_name += symbol

                if symbol == "(" or symbol == ")":
                    word_status_value = not word_status_value
                if word_status_value and not symbol == "(":
                    str_value += symbol

            if not str_name == '' and not str_value == '':
                if str_name == 'name':
                    user[str_name] = str_value
                else:
                    user[str_name] = float(str_value)

            str_name = ''
            str_value = ''
    return user

# бой не на жизнь а на смерть
def bloodbath(p1, p2):
    while p1['health'] > 0 and p2['health'] > 0:
        attack(p1, p2)
        attack(p2, p1)

# старт игры
def start_game_session():
    players = []
    players.append(render_player('qwe'))
    players.append(render_player('ewq'))
    armor(players[0], players[1])
    bloodbath(players[0], players[1])
    return players


players = start_game_session()
for i in players:
    print(i)
