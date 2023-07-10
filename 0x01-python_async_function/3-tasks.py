#!/usr/bin/env python3

"""
a function to return an async task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ a function task wait random"""
    task = asyncio.Task(wait_random(max_delay))
    return task
