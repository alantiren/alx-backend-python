#!/usr/bin/env python3
"""
Module with a type-annotated function to convert a string and int/float to a tuple.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to convert a string and int/float to a tuple.
    """
    return (k, float(v**2))
