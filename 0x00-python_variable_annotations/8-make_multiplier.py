#!/usr/bin/env python3
"""
Module with a type-annotated function to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to create a multiplier function.
    """
    def multiplier_function(x: float) -> float:
        """
        Inner function to multiply a float by the multiplier.
        """
        return x * multiplier
    return multiplier_function
