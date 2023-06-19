import asyncio


async def example_barrier():
    # 3 Barrier setting
    b = asyncio.Barrier(3)

    # create 2 new waiting task
    asyncio.create_task(b.wait())
    asyncio.create_task(b.wait())

    await asyncio.sleep(0)
    print(b)

    # third .wait() call passes the barrier
    await b.wait()
    print(b)
    print("barrier passed")

    await asyncio.sleep(0)
    print(b)


asyncio.run(example_barrier())

# <asyncio.locks.Barrier object at 0x1039d3dd0 [filling, waiters:2/3]>
# <asyncio.locks.Barrier object at 0x1039d3dd0 [draining, waiters:0/3]>
# barrier passed
# <asyncio.locks.Barrier object at 0x1039d3dd0 [filling, waiters:0/3]>
