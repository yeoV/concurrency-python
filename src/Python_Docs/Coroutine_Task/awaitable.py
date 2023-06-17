import asyncio


async def nested():
    return 42


async def main():
    # await 함수가 없을 경우 에러 발생
    # nested()
    print(await nested())

    task = asyncio.create_task(nested())

    await task


asyncio.run(main())
