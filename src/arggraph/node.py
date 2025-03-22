from __future__ import absolute_import, annotations

import re
import textwrap
import typing as t
from dataclasses import dataclass
from enum import Enum

import graphviz as gv
import networkx as nx
import pendulum

from . import dt, utils
from .utils import MISSING, MISSING_TYPE, parse, xstr


class NodeCategory(Enum):
    """Enum for types of nodes.

    - I: Information
    - RA: Inference
    - CA: Conflict
    - MA: Rephrase
    - TA: Transition
    - YA: Not used
    """

    I = "I"
    RA = "RA"
    CA = "CA"
    MA = "MA"
    TA = "TA"
    PA = "PA"
    YA = "YA"
    L = "L"


# Duplicate keys: 17, 251, 252, 61, 254, 253
ra_schemes = {
    "Alternatives (Cognitive Schemes)": 251,
    "Alternatives": 235,
    "Analogy": 1,
    "Arbitrary Verbal Classification": 59,
    "Argument From Authority": 160,
    "Argument From Goodwill": 184,
    "Argument From Moral Virtue": 182,
    "Argument From Practical Wisdom": 183,
    "Argument From Virtue/Goodwill": 402,
    "Argument From Wisdom/Goodwill": 401,
    "Argument From Wisdom/Virtue": 400,
    "Argument From Wisdom/Virtue/Goodwill": 403,
    "Bias": 2,
    "Causal Slippery Slope": 3,
    "Cause To Effect": 4,
    "Circumstantial Ad Hominem": 5,
    "Commitment": 6,
    "Composition": 236,
    "Consequences": 237,
    "Correlation To Cause": 7,
    "Danger Appeal": 17,  # ova.uni-trier.de
    # "Danger Appeal": 238, # ova.arg-tech.org
    "Definition To Verbal Classification": 239,
    "Dilemma": 9,
    "Direct Ad Hominem": 10,
    "Division": 240,
    "Established Rule": 61,
    "Ethotic": 12,
    "Evidence To Hypothesis": 13,
    "Example": 14,
    "Exceptional Case": 62,
    "Expert Opinion": 15,
    "Fairness": 254,
    "Falsification Of Hypothesis": 16,
    "Fear Appeal": 17,
    "Full Slippery Slope": 18,
    "Generic Ad Hominem": 250,
    # "Gradualism": 241, # ova.arg-tech.org
    "Gradualism": 63,  # ova.arg-tech.org
    "Ignorance": 19,
    "Inconsistent Commitment": 20,
    "Informant Report": 170,
    "Interaction Of Act And Person": 249,
    "Misplaced Priorities": 252,
    "Modus Ponens": 35,
    "Need For Help": 242,
    "Negative Consequences": 22,
    "Oppositions": 243,
    "Paraphrase": 102,
    "Perception": 244,
    "Popular Opinion": 24,
    "Popular Practice": 25,
    "Position To Know": 26,
    "Positive Consequences": 27,
    "Practical Reasoning From Analogy": 251,
    "Practical Reasoning": 28,
    "Pragmatic Argument From Alternatives": 252,
    "Pragmatic Inconsistency": 253,
    "Precedent Slippery Slope": 29,
    "Reframing": 121,
    "Rule": 61,
    "Rules": 245,
    "Sign": 30,
    "Two Person Practical Reasoning": 254,
    "Unfairness": 253,
    "Vague Verbal Classification": 60,
    "Vagueness Of Verbal Classification": 246,
    "Value Based Practical Reasoning": 81,
    "Values": 247,
    "Verbal Classification": 31,
    "Verbal Slippery Slope": 32,
    "Waste": 33,
    "Witness Testimony": 248,
}

ca_schemes = {
    "Ad hominem": 172,
    "Alternative Means": 34,
    "Biased Classification": 37,
    "Calling Out": 146,
    "Commitment Exception": 38,
    "Conflict From Goodwill": 181,
    "Conflict From Moral Virtue": 179,
    "Conflict From Practical Wisdom": 180,
    "Conflict From Virtue/Goodwill": 406,
    "Conflict From Wisdom/Goodwill": 405,
    "Conflict From Wisdom/Virtue": 404,
    "Conflict From Wisdom/Virtue/Goodwill": 407,
    "Conflicting Goals": 39,
    "Differences Undermine Similarity": 40,
    "ERAd Hominem": 164,
    "Exception Similarity Case": 41,
    "Expertise Inconsistency": 42,
    "General Acceptance Doubt": 43,
    "Irrational Fear Appeal": 44,
    "Lack Of Complete Knowledge": 45,
    "Lack Of Expert Reliability": 46,
    "Logical": 36,
    "Opposed Commitment": 48,
    "Other Causal Factors Involved": 52,
    # "Other Causal Factors Involved": 53,
    "Property Not Existant": 54,
    "Required Steps": 55,
    "Resolving Inconsistency": 56,
    "Sign From Other Events": 57,
    "Vested Interest": 171,
    "Weakest Link": 58,
}

default_schemes = {
    "Default Inference": 72,
    "RA": 72,
    "Default Conflict": 71,
    "CA": 71,
    "Default Rephrase": 144,
    "MA": 144,
    "Default Transition": 82,
    "TA": 82,
    "Default Preference": 161,
    "PA": 161,
}

schemes = {**default_schemes, **ra_schemes, **ca_schemes}
schemes = {key.lower(): value for key, value in schemes.items()}


@dataclass
class ColorMapping:
    bg: str = "#ffffff"
    fg: str = "#333333"
    border: str = "#000000"


color_mappings = {
    "r": ColorMapping(bg="#fbdedb", border="#e74c3c"),
    "g": ColorMapping(bg="#def8e9", border="#2ecc71"),
    "b": ColorMapping(bg="#ddeef9", border="#3498db"),
    "w": ColorMapping(bg="#e9eded", border="#95a5a6"),
    "y": ColorMapping(bg="#fdf6d9", border="#f1c40f"),
    "p": ColorMapping(bg="#eee3f3", border="#9b59b6"),
    "o": ColorMapping(bg="#fbeadb", border="#e67e22"),
    "t": ColorMapping(bg="#dcfaf4", border="#1abc9c"),
    "m": ColorMapping(bg="#3498db", border="#3498db"),
}


def _int2list(value: t.Optional[int]) -> t.List[int]:
    return [value] if value is not None else []


# TODO: Automatically calculate values for width, height, x and y


class Node:
    """Node in the AIF format."""

    __slots__ = (
        "_key",
        "text",
        "_raw_text",
        "category",
        "x",
        "y",
        "text_begin",
        "text_end",
        "comment",
        "descriptors",
        "cqdesc",
        "visible",
        "imgurl",
        "annotator",
        "date",
        "participant_id",
        "w",
        "h",
        "major_claim",
        "is_check_worthy",
        "source",
    )

    _key: int
    text: t.Any
    _raw_text: t.Optional[str]
    category: NodeCategory
    x: t.Optional[int]
    y: t.Optional[int]
    text_begin: t.Optional[int]
    text_end: t.Optional[int]
    comment: t.Optional[str]
    descriptors: t.Optional[t.Mapping[str, int]]
    cqdesc: t.Optional[t.Mapping[str, t.Any]]
    visible: t.Optional[bool]
    imgurl: t.Optional[str]
    annotator: t.Optional[str]
    date: t.Optional[pendulum.DateTime]
    participant_id: t.Optional[int]
    w: t.Optional[int]
    h: t.Optional[int]
    major_claim: t.Optional[bool]
    is_check_worthy: t.Optional[str]
    source: t.Optional[str]

    def __init__(
        self,
        key: int,
        text: t.Any,
        category: NodeCategory,
        raw_text: t.Optional[str] = None,
        x: t.Optional[int] = None,
        y: t.Optional[int] = None,
        text_begin: t.Optional[int] = None,
        text_end: t.Optional[int] = None,
        comment: t.Optional[str] = None,
        descriptors: t.Optional[t.Mapping[str, int]] = None,
        cqdesc: t.Optional[t.Mapping[str, t.Any]] = None,
        visible: t.Optional[bool] = None,
        imgurl: t.Optional[str] = None,
        annotator: t.Optional[str] = None,
        date: t.Union[MISSING_TYPE, None, pendulum.DateTime] = MISSING,
        participant_id: t.Optional[int] = None,
        w: t.Optional[int] = None,
        h: t.Optional[int] = None,
        major_claim: t.Optional[bool] = None,
        is_check_worthy: t.Optional[str] = None,
        source: t.Optional[str] = None,
    ):
        self._key = key
        self.text = text
        self._raw_text = raw_text
        self.category = category
        self.x = x
        self.y = y
        self.text_begin = text_begin
        self.text_end = text_end
        self.comment = comment
        self.descriptors = descriptors
        self.cqdesc = cqdesc
        self.visible = visible
        self.imgurl = imgurl
        self.annotator = annotator
        self.date = pendulum.now() if date is MISSING else date
        self.participant_id = participant_id
        self.w = w
        self.h = h
        self.major_claim = major_claim
        self.is_check_worthy = is_check_worthy
        self.source = source

        self.__post_init__()

    def __post_init__(self):
        pass

    def __repr__(self):
        return utils.class_repr(self, [str(self.key), self.plain_text])

    @property
    def key(self) -> int:
        return self._key

    @property
    def raw_text(self) -> str:
        """Get `raw_text` if available or the standard `text` as string."""

        return self._raw_text or self.plain_text

    @raw_text.setter
    def raw_text(self, value: str) -> None:
        self._raw_text = value

    @property
    def plain_text(self) -> str:
        """Get the standard `text` as string."""

        return xstr(self.text)

    @property
    def scheme(self) -> int:
        """Get argumentation scheme id based on `text`."""

        if self.category == NodeCategory.I:
            return 0

        return schemes[self.plain_text.lower()]

    @property
    def text_length(self) -> t.Optional[int]:
        """Get text length for I-nodes."""

        if self.category == NodeCategory.I:
            return len(self.plain_text)
        return None

    @property
    def ova_color(self) -> str:
        """Get the color used in OVA based on `category`."""

        if self.category == NodeCategory.I:
            if self.major_claim:
                return "m"
            else:
                return "b"
        elif self.category == NodeCategory.RA:
            return "g"
        elif self.category == NodeCategory.CA:
            return "r"
        elif self.category == NodeCategory.TA:
            return "p"
        elif self.category == NodeCategory.MA:
            return "o"
        elif self.category == NodeCategory.PA:
            return "t"
        elif self.category == NodeCategory.YA:
            return "y"
        return "w"

    @property
    def gv_color(self) -> ColorMapping:
        """Get the colors used for graphviz based on the OVA color."""

        # if self.category == NodeCategory.RA:
        #     return "palegreen"
        # elif self.category == NodeCategory.CA:
        #     return "tomato"
        # elif self.major_claim:
        #     return "lightskyblue"
        # return "aliceblue"
        return color_mappings[self.ova_color]

    @classmethod
    def from_ova(
        cls,
        obj: t.Mapping[str, t.Any],
        nlp: t.Optional[t.Callable[[str], t.Any]] = None,
    ) -> Node:
        text_begin = obj.get("text_begin") or []
        text_end = obj.get("text_end") or []
        participant_id = int(obj["participantID"]) if obj.get("participantID") else None

        return cls(
            key=obj["id"],
            text=parse(obj["text"], nlp),
            category=NodeCategory(obj["type"]),
            x=obj.get("x"),
            y=obj.get("y"),
            text_begin=next(iter(text_begin), None),
            text_end=next(iter(text_end), None),
            comment=obj.get("comment"),
            descriptors=obj.get("descriptors"),
            cqdesc=obj.get("cqdesc"),
            visible=obj.get("visible"),
            imgurl=obj.get("imgurl"),
            annotator=obj.get("annotator"),
            date=dt.from_ova(obj.get("date")),
            participant_id=participant_id,
            w=obj.get("w"),
            h=obj.get("h"),
            major_claim=obj.get("majorClaim"),
            is_check_worthy=obj.get("is_check_worthy"),
            source=obj.get("source"),
        )

    # TODO: Check fallback value for date.
    def to_ova(self) -> t.Dict[str, t.Any]:
        return {
            "id": self.key,
            "text": self.plain_text,
            "type": self.category.value,
            "x": self.x or 0,
            "y": self.y or 0,
            "text_begin": _int2list(self.text_begin),
            "text_end": _int2list(self.text_end),
            "text_length": _int2list(self.text_length),
            "comment": self.comment or "",
            "scheme": str(self.scheme),
            "descriptors": self.descriptors or {},
            "cqdesc": self.cqdesc or {},
            "visible": self.visible or True,
            "imgurl": self.imgurl or "",
            "annotator": self.annotator or "",
            "date": dt.to_ova(self.date),
            "participantID": xstr(self.participant_id) or "0",
            "w": self.w or 0,
            "h": self.h or 0,
            "majorClaim": self.major_claim or False,
            "color": self.ova_color,
            "is_check_worthy": self.is_check_worthy or "no",
            "source": self.source or "",
        }

    @classmethod
    def from_aif(
        cls,
        obj: t.Mapping[str, t.Any],
        nlp: t.Optional[t.Callable[[str], t.Any]] = None,
    ) -> Node:
        return cls(
            key=int(obj["nodeID"]),
            text=parse(obj["text"], nlp),
            category=NodeCategory(obj["type"]),
            date=dt.from_aif(obj.get("timestamp")),
        )

    def to_aif(self) -> t.Dict[str, t.Any]:
        return {
            "nodeID": str(self.key),
            "text": self.plain_text,
            "type": self.category.value,
            "timestamp": dt.to_aif(self.date),
        }

    def to_nx(self, g: nx.DiGraph) -> None:
        g.add_node(
            self.key,
            label=self.plain_text,
            # Custom attributes
            category=self.category.value,
            major_claim=self.major_claim,
        )

    def to_gv(
        self,
        g: gv.Digraph,
        labels: t.Optional[t.Iterable[str]] = None,
        color: t.Optional[ColorMapping] = None,
        label_prefix: str = "",
        label_suffix: str = "",
        key_prefix: str = "",
        key_suffix: str = "",
        wrap_col: t.Optional[int] = None,
        margin: t.Optional[t.Tuple[float, float]] = None,
        font_name: t.Optional[str] = None,
        font_size: t.Optional[float] = None,
    ) -> None:
        if not color:
            color = self.gv_color

        if not labels:
            labels = ["plain_text"]

        if not wrap_col:
            wrap_col = 36

        if not margin:
            margin = (0.15, 0.1)

        if not font_name:
            font_name = "Arial"

        if not font_size:
            font_size = 11

        label = "\n".join(str(getattr(self, attr)) for attr in labels)

        # TODO: Improve wrapping
        # https://stackoverflow.com/a/26538082/7626878
        label_wrapped = textwrap.fill(label, wrap_col)

        g.node(
            f"{key_prefix}{self.key}{key_suffix}",
            label=f"{label_prefix}\n{label_wrapped}\n{label_suffix}".strip(),
            fontname=font_name,
            fontsize=str(font_size),
            fontcolor=color.fg,
            fillcolor=color.bg,
            color=color.border,
            style="filled",
            root=str(bool(self.major_claim)),
            shape="box",
            width="0",
            height="0",
            margin=f"{margin[0]},{margin[1]}",
        )

    # def copy(self, key: int) -> Node:
    #     obj = Node.from_dict(self.to_dict(), nlp)
    #     obj._key = key
    #
    #     return obj
