from typing import List, Optional
from classes.dice import Dice
from classes.skills import CharacterSkill
import enums


class Card(object):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

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
        
class SupportCard(ActionCard):
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        cost: List[Dice],
        skin: str,
    ):
        super().__init__(id, name, description, cost, skin)

class EventCard(ActionCard):
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        cost: List[Dice],
        skin: str,
    ):
        super().__init__(id, name, description, cost, skin)

class FoodCard(ActionCard):
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        cost: List[Dice],
        skin: str,
    ):
        super().__init__(id, name, description, cost, skin)

class EquipmentCard(ActionCard):
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        cost: List[Dice],
        skin: str,
    ):
        super().__init__(id, name, description, cost, skin)

class WeaponCard(EquipmentCard):
    def __init__(self, id: int, name: str, description: str, cost: List[Dice], skin: str, damage: int):
        super().__init__(id, name, description, cost, skin)
        self.damage = damage

class ArtifactCard(EquipmentCard):
    def __init__(self, id: int, name: str, description: str, cost: List[Dice], skin: str):
        super().__init__(id, name, description, cost, skin)

class TalentCard(EquipmentCard):
    def __init__(self, id: int, name: str, description: str, cost: List[Dice], skin: str, energy_cost: int = 0):
        super().__init__(id, name, description, cost, skin)
        self.energy_cost = energy_cost

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
        
        self.artifact: Optional[ArtifactCard] = None
        self.food: Optional[FoodCard] = None
        self.weapon: Optional[WeaponCard] = None
        self.talent_equipped = False
