from typing import List
from classes.dice import Dice
import enums


class Card(object):
    def __init__(self, name: str):
        self.name = name


class CharacterCard(Card):
    def __init__(
        self,
        name: str,
        energy_cost: int,
        health: int,
        weapon_type: enums.WeaponType,
        element: enums.Element,
        team: enums.Team = enums.Team.CHARACTER,
    ):
        super().__init__(name)
        self.energy_cost = energy_cost
        self.current_energy = 0
        self.health = health
        self.current_health = health
        self.weapon_type = weapon_type
        self.element = element
        self.team = team

class ActionCard(Card):
    def __init__(
        self,
        name: str,
        description: str,
        cost: List[Dice],
    ):
        super().__init__(name)
        self.cost = cost
        self.description = description