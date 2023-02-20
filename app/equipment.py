from dataclasses import dataclass
from typing import List
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    name: str
    defence: int
    stamina_per_turn: int  # выносливость за ход


@dataclass
class Weapon:
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: int  # выносливость за удар

    @property
    def damage(self):
        pass


@dataclass
class EquipmentData:
    #  TODO содержит 2 списка - с оружием и с броней
    pass


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        #  TODO этот метод загружает json в переменную EquipmentData
        with open("../data/equipment.json", "r", encoding="utf-8") as file:
        # equipment_file = open()
            data = json.load(file)
            print(data)
            equipment_schema = marshmallow_dataclass.class_schema(data)
            print(equipment_schema)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError

    def get_weapon(self, weapon_name) -> Weapon:
        pass

    def get_armor(self, armor_name) -> Armor:
        #  TODO возвращает объект брони по имени
        pass

    def get_weapons_names(self) -> list:
        #  TODO возвращаем список с оружием
        pass

    def get_armors_names(self) -> list:
        #  TODO возвращаем список с броней
        pass



d = Equipment()
print(d.get_weapon())