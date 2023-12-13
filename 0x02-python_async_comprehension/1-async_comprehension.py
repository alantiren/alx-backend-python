#!/usr/bin/env python3
"""
1-async_comprehension.py
This module defines an asynchronous comprehension using async_generator.
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehensions
    over async_generator and returns the 10 random numbers.
    """
    return [num async for num in async_generator()]
