import asyncio
import random

queue = asyncio.Queue(maxsize=10)   # maxsize is queue is full and coroutines



async def producer(queue):
    print("Producer: Running")
    # generate work
    for _ in range(10):
        value = random()
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)

    
    await queue.put(None)
    print("Put is done")