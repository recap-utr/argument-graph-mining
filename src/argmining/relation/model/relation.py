from dataclasses import dataclass
from enum import Enum


class RelationClass(Enum):
    ATTACK = "CA"
    SUPPORT = "RA"
    NONE = "None"


@dataclass
class Relation:
    adu: str
    probability: float
    classification: RelationClass
