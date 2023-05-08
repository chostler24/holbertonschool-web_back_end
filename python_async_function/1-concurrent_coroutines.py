#!/usr/bin/env python3
"""
Asynchronously spawns `wait_random` `n` times with a specified `max_delay`.
Args:
    n (int): The number of times to call `wait_random`.
    max_delay (int): The maximum delay for each call to `wait_random`.
Returns:
    List[float]: A list of the delays (float values) in ascending order.
"""
import asyncio
from typing import List
from random import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function declaration"""
    delays = []
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
