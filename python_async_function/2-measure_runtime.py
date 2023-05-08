#!/usr/bin/env python3
"""
Measures the average execution time for `wait_n(n, max_delay)`.

Args:
    n (int): The number of times to call `wait_n`.
    max_delay (int): The maximum delay for each call to `wait_n`.

Returns:
    float: The average execution time for `wait_n(n, max_delay)`.
"""
from typing import List
import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time function declaration"""
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
