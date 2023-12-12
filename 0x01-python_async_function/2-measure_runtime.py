#!/usr/bin/env python3
"""
Module with a function to measure the total execution time for wait_n.
"""

import asyncio
import time


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
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
