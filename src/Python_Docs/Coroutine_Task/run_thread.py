# 별도의 스레드에서 func 함수를 비동기적으로 실행
import time
import asyncio


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def main():
    print(f"start main at {time.strftime('%X')}")

    await asyncio.gather(asyncio.to_thread(blocking_io), asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())
