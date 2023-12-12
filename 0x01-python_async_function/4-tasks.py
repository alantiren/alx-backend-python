#!/usr/bin/env python3
"""
Module with a function to execute multiple coroutines concurrently using asyncio tasks.
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
    tasks = []

    async def run_task_wait_random():
        nonlocal tasks
        task = task_wait_random(max_delay)
        tasks.append(task)
        await task

    await asyncio.gather(*(run_task_wait_random() for _ in range(n)))

    # Return the delays in ascending order
    return [task.result() for task in tasks]

# Testing the task_wait_n function
if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
