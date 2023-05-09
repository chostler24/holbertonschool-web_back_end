#!/usr/bin/env python3
"""
Write a function (do not create an async function, use
the regular function syntax to do this) task_wait_random
that takes an integer max_delay and returns a asyncio.Task.
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """task_wait_random function declaration"""
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
