from dataclasses import dataclass
from skills import Skill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass =  UnitClass # Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибутов

ThiefClass = UnitClass # действуем так же как и с воином

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
