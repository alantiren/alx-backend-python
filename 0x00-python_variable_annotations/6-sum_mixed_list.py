#!/usr/bin/env python3
"""
Module with a type-annotated function to sum a list of mixed integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function to sum a list of mixed integers and floats.
    """
    return float(sum(mxd_lst))
