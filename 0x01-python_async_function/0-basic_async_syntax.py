#!/usr/bin/env python3

import random
import asyncio

"""
creating and async function that returns a delay
@max_delay the maximum delay
return: a random delay
"""


async def wait_random(max_delay:int = 10) -> float:
    """wait for max_delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
