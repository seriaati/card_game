from typing import List
from classes.dice import Dice
from classes.skills import CharacterSkill
import enums


class Card(object):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class CharacterCard(Card):
    def __init__(
        self,
        id: int,
        name: str,
        energy_cost: int,
        weapon_type: enums.WeaponType,
        element: enums.Element,
        skills: List[CharacterSkill],
        faction: enums.Faction,
        skin: str,
        dynamic_skin: str,
        talent_card_id: int,
    ):
        super().__init__(id, name)
        self.energy_cost = energy_cost
        self.weapon_type = weapon_type
        self.element = element
        self.faction = faction
        self.skills = skills
        self.skin = skin
        self.dynamic_skin = dynamic_skin
        self.talent_card_id = talent_card_id
        
        self.current_energy = 0
        self.current_health = 10

class ActionCard(Card):
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        cost: List[Dice],
        skin: str
    ):
        super().__init__(id, name)
        self.cost = cost
        self.description = description
        self.skin = skin

class EquipmentCard(ActionCard):
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        cost: List[Dice],
        skin: str,
        related_character: CharacterCard,
    ):
        super().__init__(id, name, description, cost, skin)
        self.related_character = related_character

