#!/usr/bin/env python3


"""
 a wait function that returns a list of delays
 @n: number of times to call the wait function
 @max_delay: the maximum delay time
 return a list of delays
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

vector = List[float]


async def wait_n(n: int, max_delay: int) -> vector:
    """ wait function"""
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
