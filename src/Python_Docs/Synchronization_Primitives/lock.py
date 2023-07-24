import asyncio

lock = asyncio.Lock()

async with lock:
    # access shared state


####################
# 위 async with 와 동일
####################
await lock.acquire()
try:
    # access 
finally:
    lock.release()