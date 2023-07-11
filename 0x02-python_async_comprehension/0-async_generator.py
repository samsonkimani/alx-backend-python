#!/usr/bin/env python3

"""
creating an async generator async_generator
"""

import asyncio
import random


async def async_generator():
    """ an async generator functio"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
