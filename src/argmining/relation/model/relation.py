from dataclasses import dataclass
from enum import Enum


class RelationClass(Enum):
    ATTACK = "Attack"
    SUPPORT = "Support"
    NONE = "Unknown"


@dataclass(frozen=True, slots=True)
class Relation:
    adu: str
    probability: float
    classification: RelationClass
