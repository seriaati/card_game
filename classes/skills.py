from typing import List

from classes.dice import Dice
import enums


class CharacterSkill(object):
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        cost: List[Dice],
        element_apply: enums.Element,
        damage: int,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.element_apply = element_apply
        self.damage = damage
