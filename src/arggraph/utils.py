from __future__ import absolute_import, annotations

import collections
import typing as t
import uuid

# key_iterator = itertools.count(start=1)
#
#
# def keygen() -> int:
#     return next(key_iterator)


def unique_id() -> int:
    return uuid.uuid1().int >> 64


def _class_name(obj) -> str:
    return obj.__class__.__name__


def class_repr(obj, attributes: t.Iterable[str]) -> str:
    return f"{_class_name(obj)}({', '.join(attributes)})"


def xstr(data: t.Any) -> str:
    return "" if data is None else str(data)


def parse(text: str, nlp: t.Optional[t.Callable[[str], t.Any]]) -> t.Any:
    if nlp:
        try:
            out = nlp(text)
        except ValueError:
            out = nlp("")

        return out

    return text


def type_error(actual: t.Type, expected: t.Type) -> str:
    return f"Expected type '{expected}', but got '{actual}'. Make sure that you are passing the correct method arguments."


def duplicate_key_error(name: str, key: int) -> str:
    return f"Graph '{name}' already contains an element with key '{key}'. The keys have to be unique within each graph."


def missing_key_error(name: str, key: int) -> str:
    return f"Graph '{name}' does not contain an element with key '{key}'. It cannot be removed."


class MISSING_TYPE:
    """A sentinel object to detect if a parameter is supplied or not."""

    pass


MISSING = MISSING_TYPE()


T = t.TypeVar("T")
U = t.TypeVar("U")


class ImmutableList(t.Sequence[T]):
    """Read-only view."""

    __slots__ = "_store"

    _store: t.Sequence[T]

    def __init__(self, items: t.Optional[t.Sequence[T]] = None):
        self._store = items or list()

    def __len__(self) -> int:
        return self._store.__len__()

    @t.overload
    def __getitem__(self, key: int) -> T:
        pass  # Don't put code here

    @t.overload
    def __getitem__(self, key: slice) -> t.Sequence[T]:
        pass  # Don't put code here

    def __getitem__(self, key: t.Union[int, slice]) -> t.Union[T, t.Sequence[T]]:
        return self._store.__getitem__(key)

    def __repr__(self) -> str:
        return self._store.__repr__()

    def __str__(self) -> str:
        return self._store.__str__()


class ImmutableSet(t.AbstractSet[T]):
    """Read-only view."""

    __slots__ = "_store"

    _store: t.Set[T]

    def __init__(self, items: t.Optional[t.Set[T]] = None):
        self._store = items or set()

    def __len__(self) -> int:
        return self._store.__len__()

    def __contains__(self, item: object) -> bool:
        return self._store.__contains__(item)

    def __iter__(self) -> t.Iterator[T]:
        return self._store.__iter__()

    def __repr__(self) -> str:
        return self._store.__repr__()

    def __str__(self) -> str:
        return self._store.__str__()


class ImmutableDict(t.Mapping[T, U]):
    """Read-only view."""

    __slots__ = "_store"

    _store: t.Dict[T, U]

    def __init__(self, items: t.Optional[t.Dict[T, U]] = None):
        self._store = items or collections.OrderedDict()

    def __len__(self) -> int:
        return self._store.__len__()

    def __getitem__(self, key: T) -> U:
        return self._store.__getitem__(key)

    def __iter__(self) -> t.Iterator:
        return self._store.__iter__()

    def __repr__(self) -> str:
        return self._store.__repr__()

    def __str__(self) -> str:
        return self._store.__str__()
