#!/usr/bin/env python3
"""a nearly identical wait_n function implementation"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a modified implementation of wait_n
    """

    results = await asyncio.gather(*tuple(map(lambda _: task_wait_random(
        max_delay), range(n))))
    return sorted(results)
