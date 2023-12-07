#!/usr/bin/env python3
"""
Module with a type-annotated function to compute the length of elements in an iterable.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to compute the length of elements in an iterable.
    """
    return [(i, len(i)) for i in lst]
