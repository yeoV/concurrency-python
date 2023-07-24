# Queue 에 sec 변수가 들어있음
# 하나씩 꺼내어 시간만큼 Sleep

import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # 큐에서 item get (sleep 을 위한 sec)
        sleep_for = await queue.get()
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
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f"worker-{i}", q))
        tasks.append(task)

    # 큐의 모든 작업이 수행될 떄까지 wait
    started_at = time.monotonic()
    print(started_at)
    await q.join()
    print(time.monotonic())
    total_slept_for = time.monotonic() - started_at

    # Cancel out worker tasks
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled
    await asyncio.gather(*tasks, return_exceptions=True)

    print("====")
    print(f"3 workers slept in parallel for {total_slept_for:.2f} seconds")
    print(f"total expected sleep time: {total_sleep_time:.2f} seconds")


asyncio.run(main())
