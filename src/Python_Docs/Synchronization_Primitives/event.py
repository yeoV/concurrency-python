import asyncio


async def waiter(event):
    print("Waiting for it ...")
    # wait -> event 가 set 될때까지 Block
    await event.wait()
    print("... got it")


async def main():
    # Create Evnet Object
    event = asyncio.Event()

    # Event set 까지 기다림
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 sec and set the event
    await asyncio.sleep(1)
    # Evnet Flag를 참으로.
    event.set()
    # Set 된 Event 초기화
    event.clear()

    waiter_task2 = asyncio.create_task(waiter(event))
    # event.set()
    # Wait Until the waiter task is finished
    await asyncio.gather(waiter_task, waiter_task2)


asyncio.run(main())
