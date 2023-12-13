#!/usr/bin/env python3
"""
2-measure_runtime.py
This module measures the runtime of parallel async comprehensions.
"""

import asyncio
from time import perf_counter
from typing import Coroutine


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    return end_time - start_time
