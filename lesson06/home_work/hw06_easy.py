# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_polise = bool(is_polise)
    def go(self):
        print('машина модель {} поехала'.format(self.name))
    def stop(self):
        print('машина модель {} остановилась'.format(self.name))
    def turn(self, way):
        print('машина модель {} повернула {}'.format(self.name, way))


class TownCar(car):
    pass
class SportCar(car):
    pass
class WorkCar(car):
    pass
class PoliceCar(car):
    pass


a1 = TownCar(80, 'green', 'lada', False)
a2 = SportCar(80, 'black', 'bmw', False)
a3 = WorkCar(80, 'brown', 'gazelle', False)
a4 = PoliceCar(80, 'white', 'priora', True)

a1.turn('влево')
a2.stop()
a3.go()