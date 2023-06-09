import asyncio


async def task_job():
    print(f"Call Task Fucntion")


async def main():
    my_task = asyncio.create_task(task_job())


if __name__ == "__main__":
    main()
