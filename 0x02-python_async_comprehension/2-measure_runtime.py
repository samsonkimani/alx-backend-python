#!/usr/bin/env python3

"""
getting the runtime for 4 parallel comprehensions
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measuring the runtime"""
    start_time = time.time()

    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())

    end_time = time.time()

    time_taken = end_time - start_time

    return time_taken
