# 별도의 스레드에서 func 함수를 비동기적으로 실행
import time
import asyncio


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # 이 부분이 IO 코드로 변경
    time.sleep(4)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def print_hello():
    print(f"start print hello def {time.strftime('%X')}")
    print("Hello")
    time.sleep(2)


async def main():
    print(f"start main at {time.strftime('%X')}")

    await asyncio.gather(asyncio.to_thread(blocking_io), asyncio.sleep(1))
    await print_hello()

    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())


# start main at 16:03:17
# start blocking_io at 16:03:17
# blocking_io complete at 16:03:21
# start print hello def 16:03:21
# Hello
# finished main at 16:03:23
