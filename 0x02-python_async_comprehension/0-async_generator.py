#!/usr/bin/env python3
"""
0-async_generator.py
This module defines an asynchronous generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loops 10 times, waits asynchronously for 1 second each
    iteration, and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
