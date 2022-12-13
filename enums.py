from enum import Enum


class WeaponType(Enum):
    SWORD = 1
    CATALYST = 2
    BOW = 3
    CLAYMORE = 4
    POLEARM = 5
    OTHER = 6

class Element(Enum):
    PYRO = 1
    HYDRO = 2
    ELECTRO = 3
    ANEMO = 4
    GEO = 5
    CRYO = 6
    DENDRO = 7
    ALL = 8
    NONE = 9

class Team(Enum):
    MONSTER = 1
    CHARACTER = 2
