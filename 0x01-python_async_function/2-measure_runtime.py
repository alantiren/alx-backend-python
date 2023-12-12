#!/usr/bin/env python3
"""
Module with a function to measure the total execution time for wait_n.
"""

import time
from typing import Callable


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: Total execution time / n.
    """
    start_time = time.time()

    async def run_wait_n():
        await wait_n(n, max_delay)

    asyncio.run(run_wait_n())

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n

# Testing the measure_time function
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
