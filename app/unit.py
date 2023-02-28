from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Equipment, Weapon, Armor
from classes import UnitClass, FuryPunch, HardShot
from random import randint
from typing import Optional


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """
    def __init__(self, name: str, unit_class: UnitClass):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health  # очки здоровья
        self.stamina = unit_class.max_stamina  # уровень выносливости
        self.weapon = None
        self.armor = None
        self._is_skill_used = False
        # print(self.hp, 'init')
        # print(self.stamina, 'st')
        # print(self.armor, 'in')
        # print(self.weapon, 'wea')

    @property
    def health_points(self):
        # возвращаем аттрибут hp в красивом виде
        return f"Дорогой игрок {self.name} твой уровень здоровья ({self.hp})"

    @property
    def stamina_points(self):
        # возвращаем аттрибут hp в красивом виде
        return f"Дорогой игрок {self.name} твоя выносливость ({self.stamina})"

    def equip_weapon(self, weapon: Weapon):
        # присваиваем нашему герою новое оружие
        return f"Игрок {self.name} экипирован оружием {weapon.name}"

    def equip_armor(self, armor: Armor):
        # одеваем новую броню
        return f"Игрок {self.name} экипирован броней {armor.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        damage = 0
        #  TODO Эта функция должна содержать:
        #   логику расчета урона игрока
        #   логику расчета брони цели
        #   здесь же происходит уменьшение выносливости атакующего при ударе
        #   и уменьшение выносливости защищающегося при использовании брони
        #   если у защищающегося нехватает выносливости - его броня игнорируется
        #   после всех расчетов цель получает урон - target.get_damage(damage)
        #   и возвращаем предполагаемый урон для последующего вывода пользователю в текстовом виде

        target.get_damage(damage)
        return damage

    def get_damage(self, damage: int) -> Optional[int]:
        # TODO получение урона целью присваиваем новое значение для аттрибута self.hp
        # if self == 2:
        # Рандомно от 0 до 5 добавляет хп.
        self.hp -= self._count_damage(damage)
        # Если здоровье игрока больше, то хп игрока будет равна 100.
        if self.hp > 100:
            self.hp = 100

        # new_hp = damage - self.hp
        print("Ваши хп %s", self.hp)
        return self.hp

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """
        Этот метод будет переопределен ниже
        """
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        Метод использования умения.
        Если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку, которая характеризует выполнение умения
        """
        return self.unit_class.skill.use(user=self, target=target)


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        Вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        # результат функции должен возвращать следующие строки:
        if self._count_damage(target) >= self.stamina:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона." \
                   f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает." \
                   f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Функция удар соперника
        должна содержать логику применения соперником умения
        (он должен делать это автоматически и только 1 раз за бой).
        Например, для этих целей можно использовать функцию randint из библиотеки random.
        Если умение не применено, противник наносит простой удар, где также используется
        функция _count_damage(target
        """
        # TODO результат функции должен возвращать результат функции skill.use или же следующие строки:
        return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона." \
               f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает." \
               f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


un = UnitClass(name='Player', max_health=100, max_stamina=10, attack=4, stamina=10, armor=5, skill=FuryPunch())
player = PlayerUnit(name=un.name, unit_class=un)

un_en = UnitClass(name='Enemy', max_health=100, max_stamina=8, attack=7, stamina=8, armor=2, skill=HardShot())
enemy = EnemyUnit(name=un_en.name, unit_class=un_en)
ar = Equipment()
# print(player.use_skill(player))
# print(player.hit(player))
# print(player.health_points)
# print(player.stamina_points)
# print(player.equip_armor(armor=ar.get_weapons_names()))


# print(enemy.use_skill(enemy))
# print(enemy.hit(enemy))

