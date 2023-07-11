#!/usr/bin/env python3

"""
creating an async generator async_generator
"""

import asyncio
from typing import Generator
import random


async def async_generator():
    """ an async generator functio"""
    for _ in range(10):
        i = random.uniform(0, 10)
        yield i
        await asyncio.sleep(1)
