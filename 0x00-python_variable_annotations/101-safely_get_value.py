#!/usr/bin/env python3
"""
Module with type-annotated function safely_get_value.
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Function to safely get a value from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
