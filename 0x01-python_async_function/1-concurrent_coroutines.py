#!/usr/bin/env python3
"""
Module with an async routine to execute multiple coroutines concurrently.
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []

    async def run_wait_random():
        nonlocal delays
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(run_wait_random() for _ in range(n)))

    # Return the delays in ascending order
    return sorted(delays)

# Testing the async routine
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
