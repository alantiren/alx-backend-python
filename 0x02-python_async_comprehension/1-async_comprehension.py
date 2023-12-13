#!/usr/bin/env python3
"""
1-async_comprehension.py
This module defines an asynchronous comprehension using async_generator.
"""

from typing import List, AsyncGenerator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehensions
    over async_generator and returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
