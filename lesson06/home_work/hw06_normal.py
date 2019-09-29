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
import random
class person:
    def __init__(self, name):
        self.name = name
        self.ammo  = 500
        self.health  = 100
        self.damage = 20
        self.armor =100
    def attack(self, ob1):
        udar = random.randint(10, self.damage)
        ob1.__uron__(udar)
    def __uron__(self, dam):
        if  self.armor != 0:
            self.armor  -= dam
            if  self.armor < 0:
                self.health += self.armor
                self.armor = 0
        else:
            self.health  -= dam


    def status(self):
        print('осталось брони {} жизней {}'.format( self.armor,  self.health))

class player(person):
    pass
class enemy(person):
    pass

P1 = player('miha')
P2 = enemy('john')

while P1.health > 0 and P2.health  > 0:
    P1.attack(P2)
    P1.status()
    P2.status()
    P2.attack(P1)
    P1.status()
    P2.status()