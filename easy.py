# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    pass


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
    pass


town_car = TownCar(80, 'grey', 'Gim')
# town_car.go()
print(f'speed: {town_car.speed},\ncolor: {town_car.color},\nname: {town_car.name},\nis_police: {town_car.is_police}')
