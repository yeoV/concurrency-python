# Queue 에 sec 변수가 들어있음
# 하나씩 꺼내어 시간만큼 Sleep

import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # queue.get()
        try:
            sleep_for = queue.get_nowait()
        except asyncio.QueueEmpty:
            break
        print(f"sleep_for : {sleep_for}")

        await asyncio.sleep(sleep_for)

        # Notify the queue work item has been processed
        queue.task_done()

        print(f"{name} has slept for {sleep_for:.2f} seconds")


async def main():
    # Create Quere
    q = asyncio.Queue()

    total_sleep_time = 0
    for _ in range(20):
        # sleep_for = random.uniform(0.05, 1.0)
        sleep_for = 1
        total_sleep_time += sleep_for
        # block 하지 않고 큐에 즉시 넣음.
        # 큐 가득찰 경우 QueueFull
        q.put_nowait(sleep_for)

    # Create 3 workers
    # async with 구문은 모든 task가 종료되어야 함
    async with asyncio.TaskGroup() as tg:
        started_at = time.monotonic()
        for idx in range(3):
            tg.create_task(worker(f"worker-{idx}", q))
        await q.join()

    # 큐의 모든 작업이 수행될 떄까지 waits
    # await 메소드가 없어 모든 task가 종료되기까지 기다리지 않음
    # 큐의 모든 내용이 종료되는 것을 보장하지 못함
    print(time.monotonic())
    total_slept_for = time.monotonic() - started_at

    print("====")
    print(f"3 workers slept in parallel for {total_slept_for:.2f} seconds")
    print(f"total expected sleep time: {total_sleep_time:.2f} seconds")


asyncio.run(main())
