#!/usr/bin/env python3
"""
Module with duck-typed annotations for safe_first_element.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function to safely get the first element of a sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
