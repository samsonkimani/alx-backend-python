#!/usr/bin/env python3

"""
write an async comprehension
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ async generator"""
    return [i async for i in async_generator()]
