import asyncio
import time

# 1초 기다린 후 결과를 출력하는 코루틴 함수


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    # 순차적으로 동기 처리
    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}")


"""
async 키워드를 통하여 동시에 처리
"""


async def async_main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # Wait Both tasks are completed
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
asyncio.run(async_main())

####################### main() 결과화면 #########################
# started at 18:10:04
# hello
# world
# finidhed at 18:10:07
####################### async_main() 결과화면 ################### -> 약 2초정도 소요
# started at 18:15:34
# hello
# world
# finished at 18:15:36
###############################################################

# Python 3.11 버전 추가 : asyncio.TaskGroup -> Task 관리 매니저
# async with -> 그룹의 모든 task가 finish 될 때까지 wait
# TaskGroup에 create_task를 통하여 Task add


async def taskgroup_main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(1, "hello"))

        task2 = tg.create_task(say_after(2, "world"))
