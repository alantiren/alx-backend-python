#!/usr/bin/env python3
"""
Module with a regular function to create an asyncio.Task.
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine with the specified max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

# Testing the task_wait_random function
if __name__ == "__main__":
    async def test(max_delay: int):
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
