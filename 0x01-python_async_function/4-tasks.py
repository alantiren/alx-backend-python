#!/usr/bin/env python3
"""
Module with a function to execute multiple coroutines concurrently
using asyncio tasks.
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines concurrently using asyncio tasks.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
