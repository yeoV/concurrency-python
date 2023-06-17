import asyncio


# async with function 은 모든 task그룹이 끝날때 까지 기다림.
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task()
        task2 = tg.create_task()
    print("Both tasks have completed now")


# Sleep
