from enum import Enum


class WeaponType(Enum):
    SWORD = "Sword"
    CATALYST = "Catalyst"
    BOW = "Bow"
    CLAYMORE = "Claymore"
    POLEARM = "Polearm"
    OTHER = "Other"

class Element(Enum):
    PYRO = "Pyro"
    HYDRO = "Hydro"
    ELECTRO = "Electro"
    ANEMO = "Anemo"
    GEO = "Geo"
    CRYO = "Cryo"
    DENDRO = "Dendro"
    ALL = "All"
    NONE = "None"

class Faction(Enum):
    MONDSTAT = "Mondstat"
    LIYUE = "Liyue"
    INAZUMA = "Inazuma"
    SUMERU = "Sumeru"
    FATUI = "Fatui"
    HILICHURL = "Hilichurl"
    MONSTER = "Monster"
    OTHER = "Other"
